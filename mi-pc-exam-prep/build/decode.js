/* ---------- embedded data: base85 text, raw deflate (tiny-inflate, MIT) ---------- */
const TINF = (function(){ var module = {exports:{}};
/*@@TINF@@*/
return module.exports; })();
const B85A = '/*@@B85@@*/';
const B85T = (()=>{ const t=new Int16Array(128).fill(-1); for(let i=0;i<85;i++) t[B85A.charCodeAt(i)]=i; return t; })();
function b85decode(s, n){
  s=s.replace(/\s+/g,''); const out=new Uint8Array(Math.ceil(s.length/5)*4); let o=0;
  for(let i=0;i+4<s.length;i+=5){ let v=0; for(let j=0;j<5;j++) v=v*85+B85T[s.charCodeAt(i+j)]; out[o++]=v>>>24; out[o++]=(v>>>16)&255; out[o++]=(v>>>8)&255; out[o++]=v&255; }
  return out.subarray(0, n!=null ? n : o);
}
function decodeBlock(el){
  const enc=el.getAttribute('data-enc')||'b64', txt=el.textContent; let u;
  if(enc==='b85') u=b85decode(txt, +el.getAttribute('data-len'));
  else { const s=atob(txt.trim()); u=new Uint8Array(s.length); for(let i=0;i<s.length;i++) u[i]=s.charCodeAt(i); }
  const z=el.getAttribute('data-z'); if(z){ const out=new Uint8Array(+z); TINF(u, out); u=out; }
  return u.buffer.slice(u.byteOffset, u.byteOffset+u.byteLength);
}
function loadData(){ const el=document.getElementById('data'); if(el.type==='application/json') return JSON.parse(el.textContent); return JSON.parse(new TextDecoder().decode(decodeBlock(el))); }
