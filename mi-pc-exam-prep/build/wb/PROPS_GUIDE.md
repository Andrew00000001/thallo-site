# Writing sketch props (hand-drawn whiteboard drawings)

Scratchpad root `S` = /tmp/claude-0/-home-user-thallo-site/e971c816-8cd7-5b02-909e-28368863e9bd/scratchpad ; engine dir `S/wb`.
The lesson videos draw scenes on a whiteboard (light mode) / chalkboard (dark mode) with rough.js. A **prop** is a small
reusable drawing (house, car, deer, gavel...). Read `S/wb/sketch.js` (engine, class `Ctx`) and `S/wb/props_core.js`
(existing props: copy their style) before starting. Do NOT edit those two files.

## Prop shape
```js
(()=>{ const P = SK.PROPS;
P.deer = {w:90, h:80, dh:16,                 // natural drawing box (your own units) and default height in canvas units (canvas is 160 x 80)
  anchors:{head:o=>[70,12]},                  // optional named points (bubble tails point at 'head', arrows use the box)
  draw(c, o, el){ ... } };                    // o = the element's opt object (variants), el = full element
})();
```
Draw only with the context `c` (coordinates in your w x h box, y down):
- `c.line(x1,y1,x2,y2,o)`, `c.poly([[x,y],...],o)` (closed; `{open:true}` for a polyline), `c.rect(x,y,w,h,o)`, `c.rrect(x,y,w,h,r,o)`,
  `c.curve([[x,y],...],o)` (smooth open curve through points), `c.blob([[x,y],...],o)` (smooth closed shape),
  `c.ellipse(cx,cy,w,h,o)`, `c.circle(cx,cy,diameter,o)`, `c.dot(cx,cy,d,o)`, `c.arc(cx,cy,w,h,startDeg,endDeg,o)` (0 = right, clockwise),
  `c.text(x,y,str,{size,color,align})` (handwriting font; y = baseline), `c.sub(cx,cy,height,'propName',opt)` (nest another prop).
- Style options `o`: `color` (outline: ink blue red green orange purple yellow gray brown sky pink teal white paper; default = element color,
  normally ink), `fill` (a color: hand-hatched fill), `fs:'solid'` (flat fill; use for small accents, or `fill:'paper', fs:'solid'` to
  hide lines behind a shape), `gap` (hatch spacing, default 13; smaller = denser, use 5-10 for small shapes), `cls:'thin'|'bold'|'soft'`
  (`soft` = lighter fill), `rough` (wobble, default 1; 0.4-0.7 for small precise parts), `single:true` (one stroke instead of two).
- Deterministic only: never use Math.random or Date.

## Style rules (keep the set consistent)
- Simple, iconic, instantly recognizable at small size (drawn ~10-30 canvas units tall, i.e. 60-200 px). 5-25 shapes. No tiny detail.
- Black/ink outlines; color only through hatch fills (`fill:'red'`) and small solid accents. Windows: `fill:'sky', gap:6-8, cls:'soft'`.
- Front or 3/4-side view like a children's-book whiteboard doodle. Vehicles face right (the element can `flip`).
- Offer useful variants via `o` (e.g., `o.broken`, `o.color`, `o.n`), each documented in a one-line comment above the prop.
- Text inside props only when it IS the object (a sign, a label on a document); keep it short.

## Check your work visually (required)
```
cd S/wb
python3 tools/mklab.py --props props_core.js,<your file> --out lab_<yourname>.html
node tools/shot.js --gallery shots_<yourname>.png --lab lab_<yourname>.html --cols 6 --px 6 --only a,b,c
node tools/shot.js --gallery shots_<yourname>_dark.png --lab lab_<yourname>.html --cols 6 --px 6 --only a,b,c --theme dark
```
Then Read the PNGs and look at every prop. Fix anything that is not instantly recognizable, lopsided, overflowing its box, or ugly.
Also try a few variants in a scene (write a spec JSON `{"elements":[{"p":"deer","x":40,"y":40,"h":20,"opt":{...}}]}` and run
`node tools/shot.js spec.json out.png --lab lab_<yourname>.html`). Iterate until every prop looks good in both themes.
The output JSON lists `errors` (JS errors): it must be empty.
