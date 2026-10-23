"""Convert Lucide SVG icons to lists of SVG path strings (rough.js can only roughen path data)."""
import re, os, json, sys
def attrs(tag):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', tag))
def to_paths(svg):
    out = []
    for tag in re.findall(r'<(path|circle|rect|line|polyline|polygon|ellipse)\b([^>]*)/?>', svg):
        kind, a = tag[0], attrs(tag[1])
        f = lambda k, d=0: float(a.get(k, d))
        if kind == 'path': out.append(a['d'])
        elif kind == 'circle':
            cx, cy, r = f('cx'), f('cy'), f('r'); out.append(f'M{cx-r} {cy}a{r} {r} 0 1 0 {2*r} 0a{r} {r} 0 1 0 {-2*r} 0')
        elif kind == 'ellipse':
            cx, cy, rx, ry = f('cx'), f('cy'), f('rx'), f('ry'); out.append(f'M{cx-rx} {cy}a{rx} {ry} 0 1 0 {2*rx} 0a{rx} {ry} 0 1 0 {-2*rx} 0')
        elif kind == 'rect':
            x, y, w, h, r = f('x'), f('y'), f('width'), f('height'), f('rx', a.get('ry', 0))
            r = min(r, w/2, h/2)
            if r: out.append(f'M{x+r} {y}h{w-2*r}a{r} {r} 0 0 1 {r} {r}v{h-2*r}a{r} {r} 0 0 1 {-r} {r}h{-(w-2*r)}a{r} {r} 0 0 1 {-r} {-r}v{-(h-2*r)}a{r} {r} 0 0 1 {r} {-r}z')
            else: out.append(f'M{x} {y}h{w}v{h}h{-w}z')
        elif kind == 'line': out.append(f"M{f('x1')} {f('y1')}L{f('x2')} {f('y2')}")
        else:
            pts = re.findall(r'-?[\d.]+', a['points']); pp = ' '.join(f'{pts[i]} {pts[i+1]}' for i in range(0, len(pts), 2))
            out.append('M' + pp.replace(' ', ' ', 1) + ('z' if kind == 'polygon' else ''))
    return out
if __name__ == '__main__':
    d = sys.argv[1]; names = sys.argv[3:] or [n[:-4] for n in os.listdir(d) if n.endswith('.svg')]
    res = {n: to_paths(open(os.path.join(d, n + '.svg')).read()) for n in sorted(names) if os.path.exists(os.path.join(d, n + '.svg'))}
    json.dump(res, open(sys.argv[2], 'w'), separators=(',', ':')); print(len(res), 'icons')
