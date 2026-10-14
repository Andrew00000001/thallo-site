// BBG News relay (Cloudflare Worker).
// Receives the "Send to BBG News" Discord command, asks the owner for the credit and the
// player's OK, then hands the clip link to the GitHub Actions bot, which posts the Reel.
// It never downloads the clip itself (Discord blocks Cloudflare Workers from attachment links).
//
// Setup: paste this whole file into the Worker's code editor, then add one Secret named
// GH_TOKEN (a GitHub token that can run this repo's workflows).

const OWNER_ID = "";            // your Discord user ID: only you can use the app
const DISCORD_PUBLIC_KEY = "";  // Developer Portal > General Information > Public Key
const GITHUB_REPO = "Andrew00000001/bbg-news";
const WORKFLOW_FILE = "bbg-news.yml";
const COMMAND_NAME = "Send to BBG News";
const VIDEO_EXT = /\.(mp4|mov|m4v|webm|mkv)$/i;
const CLIP_URL = /^https:\/\/(cdn\.discordapp\.com|media\.discordapp\.net)\/attachments\/\d+\/\d+\/[^\s/]+$/;
const DISCORD_UA = `DiscordBot (https://github.com/${GITHUB_REPO}, 1.0)`;

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });
const privateReply = (content) => json({ type: 4, data: { content, flags: 64 } });

function hex(s) {
  if (!/^(?:[0-9a-f]{2})+$/i.test(s || "")) throw new Error("not hex");
  return new Uint8Array(s.match(/../g).map((b) => parseInt(b, 16)));
}

// Discord signs every request; it also sends bad signatures on purpose and expects a 401.
async function verified(request, body) {
  try {
    const key = await crypto.subtle.importKey("raw", hex(DISCORD_PUBLIC_KEY), { name: "Ed25519" }, false, ["verify"]);
    const signed = new TextEncoder().encode((request.headers.get("X-Signature-Timestamp") || "") + body);
    return await crypto.subtle.verify("Ed25519", key, hex(request.headers.get("X-Signature-Ed25519")), signed);
  } catch {
    return false;
  }
}

function findVideo(msg) {
  // Forwarded messages carry their files in message_snapshots.
  const lists = [msg.attachments || [], ...(msg.message_snapshots || []).map((s) => s.message?.attachments || [])];
  for (const list of lists) {
    for (const a of list) {
      if ((a.content_type || "").startsWith("video/") || VIDEO_EXT.test(a.filename || "")) return a;
    }
  }
  return null;
}

function suggestedCredit(msg, invoker) {
  // Forwards and bot/webhook posts don't tell us who recorded the clip: leave it for you to fill in.
  if (msg.message_snapshots?.length || msg.webhook_id || msg.author?.bot) return "";
  if (msg.author?.id === invoker) return "BBG News";
  return (msg.author?.global_name || msg.author?.username || "").slice(0, 60);
}

function clipForm(url, credit) {
  const creditInput = { type: 4, custom_id: "credit", style: 1, max_length: 60, required: true };
  if (credit) creditInput.value = credit;
  return json({
    type: 9,
    data: {
      custom_id: "bbg-send",
      title: "Send to BBG News",
      components: [
        { type: 18, label: "Credit", description: "Shown on the Reel. Use @handle for their Instagram, or BBG News for your own clip.", component: creditInput },
        { type: 18, label: "Caption (optional)", component: { type: 4, custom_id: "caption", style: 2, max_length: 1000, required: false } },
        { type: 18, label: "Permission", component: { type: 22, custom_id: "consent", required: true, options: [{ value: "yes", label: "The player said I can post this (or it's mine)" }] } },
        { type: 18, label: "Clip link (leave as is)", component: { type: 4, custom_id: "url", style: 2, required: true, value: url } },
      ],
    },
  });
}

function submitted(data, id) {
  for (const row of data.components || []) {
    for (const c of [row.component, ...(row.components || [])]) {
      if (c?.custom_id === id) return c.values ?? c.value;
    }
  }
  return undefined;
}

async function editReply(appId, token, content) {
  await fetch(`https://discord.com/api/v10/webhooks/${appId}/${token}/messages/@original`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json", "User-Agent": DISCORD_UA },
    body: JSON.stringify({ content }),
  });
}

async function sendToGitHub(env, interaction, clip) {
  let content;
  try {
    const r = await fetch(`https://api.github.com/repos/${GITHUB_REPO}/actions/workflows/${WORKFLOW_FILE}/dispatches`, {
      method: "POST",
      headers: {
        Accept: "application/vnd.github+json",
        Authorization: `Bearer ${env.GH_TOKEN}`,
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "bbg-news-relay",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ref: "main",
        inputs: { ...clip, notify: `${interaction.application_id}/${interaction.token}` },
      }),
    });
    content = r.ok
      ? "✅ Sent to BBG News. This message updates when the Reel is live (usually within 10 minutes)."
      : `❌ GitHub didn't accept it (HTTP ${r.status}). Check the relay's GH_TOKEN, then try again.`;
  } catch {
    content = "❌ Couldn't reach GitHub. Try again in a minute.";
  }
  await editReply(interaction.application_id, interaction.token, content);
}

export default {
  async fetch(request, env, ctx) {
    if (request.method !== "POST") return new Response("BBG News relay is running.");
    const body = await request.text();
    if (!(await verified(request, body))) return new Response("invalid request signature", { status: 401 });
    const interaction = JSON.parse(body);

    if (interaction.type === 1) return json({ type: 1 }); // PING when the endpoint URL is saved

    const invoker = (interaction.member?.user || interaction.user || {}).id;
    if (invoker !== OWNER_ID) return privateReply("This app is private to BBG News.");

    // The message command: open the form.
    if (interaction.type === 2 && interaction.data?.name === COMMAND_NAME) {
      const msg = interaction.data.resolved?.messages?.[interaction.data.target_id];
      const video = msg && findVideo(msg);
      if (!video) return privateReply("That message has no video file attached. (Clips shared as links can't be sent.)");
      return clipForm(video.url, suggestedCredit(msg, invoker));
    }

    // The form was submitted.
    if (interaction.type === 5 && interaction.data?.custom_id === "bbg-send") {
      const consent = submitted(interaction.data, "consent");
      if (!(Array.isArray(consent) && consent.includes("yes"))) {
        return privateReply("Not sent: tick the permission box once the player says yes.");
      }
      const url = String(submitted(interaction.data, "url") || "").trim();
      if (!CLIP_URL.test(url.split("?")[0])) return privateReply("Not sent: the clip link was changed. Use the app on the message again.");
      const clip = {
        clip_url: url,
        credit: String(submitted(interaction.data, "credit") || "").trim().slice(0, 60),
        caption: String(submitted(interaction.data, "caption") || "").trim().slice(0, 1000),
      };
      ctx.waitUntil(sendToGitHub(env, interaction, clip));
      return json({ type: 5, data: { flags: 64 } }); // "thinking…" (private), edited once GitHub answers
    }

    return privateReply("Unknown request.");
  },
};
