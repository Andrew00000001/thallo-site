"""Write PROPS_CATALOG.md (prop names, sizes, options) and render picture sheets catalog/<file>-<n>.png for the writers."""
import glob, os, re, subprocess, json
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DOC = {
 'person': 'a person (stick figure). opt: who (dana sam jen tony rosa kid adjuster judge thief worker doctor boss neighbor grandma regulator person), pose (stand wave point shrug cheer think hold sad run stop sit walk), mood (happy smirk sad worried angry shocked laugh neutral sleep), hold (a prop name held in the hand: money policy phone clipboard check ...), sign (short text on a sign they hold), plus look overrides: hair (short spiky curly bob long pony bun none), hairColor, shirt (color), hat (cap hardhat chef beanie top), glasses, beard, mustache, tie, badge, apron, vest, coat, robe, mask, stripes. Anchors: head (bubble tails), hand.',
 'house': 'house. opt: roof (color), wall (color), garage (true: attached garage on the right). Anchors: door, roof, chimney.',
 'shed': 'detached shed (other structure). opt: roof (color)', 'store': 'shop with awning. opt: name (sign text), awning (color)',
 'insurer': 'the insurance company building. opt: name (default "INSURANCE CO.")', 'office': 'office tower. opt: name', 'factory': 'factory with chimney. opt: name',
 'apartment': 'apartment building', 'car': 'car facing right. opt: color, dent (true)', 'truck': 'box truck. opt: color', 'semi': 'semi tractor-trailer. opt: color, trailer (color), name',
 'tree': 'tree', 'fire': 'flames (add loop: "flicker")', 'smoke': 'smoke blob', 'cloud': 'cloud. opt: dark', 'rain': 'rain cloud', 'storm': 'storm cloud with lightning',
 'lightning': 'lightning bolt', 'snow': 'snowflake', 'sun': 'sun', 'wind': 'wind gusts', 'water': 'water waves strip (wide). opt: fill (false: no hatch)',
 'money': 'stack of bills', 'bill': 'one dollar bill', 'coins': 'coin stack', 'moneybag': 'money bag', 'policy': 'policy document. opt: title (header text, default POLICY), tsize, tcolor, sign (true: signature line signed)',
 'paper': 'same as policy', 'clipboard': 'clipboard checklist', 'bankcheck': 'bank check (paper check). opt: amount (text)', 'calendar': 'calendar page. opt: n (big number or short text), label (month text on the red bar), size',
 'clock': 'clock. opt: h (hour), m (minute)', 'shield': 'protection shield. opt: color, check (false hides the check mark), markColor', 'umbrella': 'umbrella. opt: color', 'phone': 'smartphone',
}
def props_in(path):
    src = open(path).read(); out = []
    lines = src.split('\n')
    for i, l in enumerate(lines):
        for m in re.finditer(r'\bP\.([a-z][a-z0-9_]*)\s*=\s*(\{|P\.)', l):
            name = m.group(1); doc = []
            j = i - 1
            while j >= 0 and lines[j].strip().startswith('//'):
                doc.insert(0, lines[j].strip()[2:].strip()); j -= 1
            tail = re.search(r'//\s*(.+)$', l[m.end():])
            if tail: doc.append(tail.group(1))
            mm = re.search(r'\bw\s*:\s*([\d.]+)\s*,\s*h\s*:\s*([\d.]+)(?:\s*,\s*dh\s*:\s*([\d.]+))?', l[m.end():m.end()+80])
            out.append((name, ' '.join(doc), mm.groups() if mm else None))
    return out
md = ['# Sketch prop catalog', '', 'Use these names as `"p"` in drawing elements. Size: give `h` (or `w`) in canvas units; `dh` is the default height.',
      'Look at the picture sheets in `S/wb/catalog/` to see each prop. Any Lucide icon is also available as `{"p":"icon","name":"..."}`.', '']
os.makedirs(os.path.join(W, 'catalog'), exist_ok=True)
import sys
FILES = [os.path.join(W, x) for x in sys.argv[1:]] or sorted(glob.glob(os.path.join(W, 'props_*.js')))
subprocess.run(['python3', os.path.join(W, 'tools', 'mklab.py'), '--props', ','.join(os.path.basename(f) for f in FILES), '--out', 'lab_catalog.html'], check=True)
for f in FILES:
    base = os.path.basename(f)[6:-3]
    ps = props_in(f)
    md += [f'## {base} ({len(ps)} props; pictures: catalog/{base}-*.png)', '', '| prop | aspect w:h, default h | notes and options |', '|---|---|---|']
    PRIMS = {'label','num','note','stamp','box','circle','check','cross','line','divider','arrow','bubble','ring','xout','icon'}
    ps = [x for x in ps if x[0] not in PRIMS]   # those names draw the built-in primitive; aliases (parcel, diamondring) cover them
    for name, doc, g in ps:
        d = CORE_DOC.get(name, doc) if base == 'core' else doc
        md.append(f'| `{name}` | {g[0]}:{g[1]}, {g[2] or "?"} | {d.replace("|", "/")} |' if g else f'| `{name}` | | {d.replace("|", "/")} |')
    md.append('')
    names = [p[0] for p in ps]
    for k in range(0, len(names), 18):
        chunk = names[k:k+18]
        subprocess.run(['node', os.path.join(W, 'tools', 'shot.js'), '--gallery', os.path.join(W, 'catalog', f'{base}-{k//18+1}.png'), '--lab', 'lab_catalog.html', '--cols', '6', '--px', '5', '--only', ','.join(chunk)], check=True, capture_output=True)
open(os.path.join(W, 'PROPS_CATALOG.md'), 'w').write('\n'.join(md)); print('catalog written')
