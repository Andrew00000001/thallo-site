"""Build the stand-alone website (Firebase Hosting, mi-pc-exam-prep.firebaseapp.com) into ../site.

The website is the same app as index.html with three differences:
- lesson audio is linked as files next to the page (lessons/LXX.lq.webm compact copies, lessons/LXX.hq.webm full quality)
  instead of being built into the page, so the page stays small;
- site-src/firebase.html and site-src/cloud.js are added right after the data: they load Firebase (Google sign-in and a
  Firestore document per person) and offer the app the same storage it uses inside Claude, so progress follows the
  Google account;
- site-src/head.html gives it a home-screen name, icons and a manifest (site-src/static).

usage (from mi-pc-exam-prep):  python3 build/site.py      then deploy (Firebase CLI, signed in to the account that owns the project):  firebase deploy --only hosting
"""
import json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, 'site-src')
OUT = os.path.join(ROOT, 'site')

env = dict(os.environ, RES='content', LEARN='content/learn', LESSONS='content/lessons', AUDIO='lessons', ICONS='build/icons',
           VALIDATOR='build', WB='build/wb', EMBED_AUDIO='0', LINK_AUDIO_LQ='1', HQ_AUDIO='1')
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, 'lessons'))
body_path = os.path.join(OUT, 'body.html')
r = subprocess.run([sys.executable, os.path.join(HERE, 'build.py'), body_path], cwd=ROOT, env=env)
if r.returncode: sys.exit(r.returncode)

body = open(body_path, encoding='utf-8').read()
lines = body.split('\n')
k = next(i for i, l in enumerate(lines) if l.startswith('<script id="data" '))
site_js = open(os.path.join(SRC, 'firebase.html'), encoding='utf-8').read() + '<script>\n' + open(os.path.join(SRC, 'cloud.js'), encoding='utf-8').read() + '</script>'
lines[k + 1:k + 1] = site_js.split('\n')
page = open(os.path.join(SRC, 'head.html'), encoding='utf-8').read() + '\n'.join(lines).rstrip('\n') + '\n</body>\n</html>\n'
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)

files = json.load(open(body_path + '.hq.json'))   # published path -> local audio file (full-quality and compact copies)
for pub, src in files.items(): shutil.copyfile(src, os.path.join(OUT, pub))
for f in os.listdir(os.path.join(SRC, 'static')): shutil.copyfile(os.path.join(SRC, 'static', f), os.path.join(OUT, f))
os.remove(body_path); os.remove(body_path + '.hq.json')
size = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(OUT) for f in fs)
print(f'site: index.html {os.path.getsize(os.path.join(OUT, "index.html")) / 1024:.0f} KB, {len(files)} audio files, {size / 1048576:.1f} MB in {OUT}')
