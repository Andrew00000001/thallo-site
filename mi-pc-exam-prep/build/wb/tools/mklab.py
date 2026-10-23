"""Build wb/lab.html: a standalone page that renders sketch specs (for screenshots and the prop gallery)."""
import base64, glob, json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: open(os.path.join(W, p)).read()
font = base64.b64encode(open(os.path.join(W, 'lib/hand.woff2'), 'rb').read()).decode()
sk = rd('sketch.js').replace('/*@@CHARW@@*/null', rd('lib/charw.json'))
import sys
argv = sys.argv[1:]; get = lambda k: argv[argv.index(k)+1] if k in argv else None
pf = get('--props'); OUTN = get('--out') or 'lab.html'
files = [os.path.join(W, x) for x in pf.split(',')] if pf else sorted(glob.glob(os.path.join(W, 'props_*.js')))
props = '\n'.join(open(p).read() for p in files)
icons = rd('lib/icons_all.json')
html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Sketch lab</title><style>
@font-face{{font-family:'SketchHand';src:url(data:font/woff2;base64,{font}) format('woff2');font-display:block}}
:root{{--f-hand:'SketchHand','Patrick Hand','Comic Sans MS',cursive;--f-display:'Archivo','Arial Narrow',Arial,sans-serif}}
{rd('sketch.css')}
html,body{{margin:0;background:var(--mk-bg);color:var(--mk-ink)}}
#stage{{position:relative;background:var(--mk-bg) radial-gradient(var(--mk-dots) 1.5px,transparent 1.6px) 0 0/22px 22px}}
.cell{{display:inline-block;vertical-align:top;margin:0;border:1px dashed var(--mk-dots)}}
.cell p{{margin:0;font:13px monospace;text-align:center;color:var(--mk-muted)}}
</style></head><body class="sk-static"><div id="stage"></div>
<script>{rd('lib/rough.js')}</script>
<script>const DATA={{skicons:{icons}}};</script>
<script>{sk}</script>
<script>{props}</script>
<script>
window.renderScene = function(spec, px){{
  const st=document.getElementById('stage'); st.innerHTML=''; const w=spec.w||160, h=spec.h||80;
  st.style.width=(w*px)+'px'; st.style.height=(h*px)+'px';
  const R=SK.render(spec.elements||spec, {{w, h, key:spec.key||'lab'}}); st.appendChild(R.svg); SK.showAll(R);
  return SK.bboxes(R);
}};
window.renderGallery = function(names, px, cols){{
  const st=document.getElementById('stage'); st.innerHTML=''; st.style.width=(cols*44*px)+'px'; st.style.height='auto';
  names.forEach(n=>{{ const d=document.createElement('div'); d.className='cell'; d.style.width=(44*px-2)+'px';
    const P=SK.PROPS[n.p]||{{w:1,h:1}}, wide=P.w/P.h>36/24; const R=SK.render([{{p:n.p, x:20, y:17, h:wide?undefined:(n.h||24), w:wide?36:undefined, opt:n.opt||{{}}}}], {{w:40, h:34, key:'g'+n.p}}); R.svg.style.height=(34*px)+'px'; d.appendChild(R.svg); SK.showAll(R);
    const p=document.createElement('p'); p.textContent=n.label||n.p; d.appendChild(p); st.appendChild(d); }});
}};
window.propList = () => Object.keys(SK.PROPS);
</script></body></html>"""
open(os.path.join(W, OUTN), 'w').write(html); print(OUTN, len(html)//1024, 'KB')
