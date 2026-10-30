"""Paint Oliver's red knee bands (each with one silver-ringed stud) onto G05 v3
(job defdbbab). The Oct 30 review panel's only soul fail on this take was the
missing bands. Usage: python3 -I fix_p14_kneebands.py IN.png OUT.png [PREVIEW.png]"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage

src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
A = np.asarray(im).astype(np.float32)
H, W, _ = A.shape
warm = A[..., 0] - A[..., 2]
lum = A.mean(-1)

# legs: (x window, band centre y at the leg's middle, band height, arc, stud dx as fraction of half width)
LEGS = [((800, 935), 1152, 26, 4, 0.10), ((940, 1062), 1158, 26, 4, 0.05)]
BAND = np.array([158, 40, 56], np.float32)
SS = 4  # supersampling

out_a = A.copy()
for (x0, x1), yc0, bh, arc, sdx in LEGS:
    y0, y1 = yc0 - 40, yc0 + 40
    sub = warm[y0:y1, x0:x1] > 30
    sub = ndimage.binary_closing(sub, iterations=3)
    sub = ndimage.binary_fill_holes(sub)
    lab, n = ndimage.label(sub)
    if n > 1:  # keep the biggest blob (the leg)
        sizes = ndimage.sum(sub, lab, range(1, n + 1))
        sub = lab == (1 + int(np.argmax(sizes)))
    # leg span on the band rows
    rows = sub[40 - bh:40 + bh]
    cols = np.where(rows.any(0))[0]
    lx0, lx1 = x0 + cols.min(), x0 + cols.max()
    xm, hw = (lx0 + lx1) / 2, (lx1 - lx0) / 2
    # supersampled band coverage
    hh, ww = (y1 - y0) * SS, (x1 - x0) * SS
    yy, xx = np.mgrid[0:hh, 0:ww]
    X = x0 + (xx + 0.5) / SS
    Y = y0 + (yy + 0.5) / SS
    u = np.clip((X - xm) / hw, -1, 1)
    yc = yc0 - arc * (1 - u ** 2)
    cover = ((Y > yc - bh / 2) & (Y < yc + bh / 2)).astype(np.float32)
    cover = cover.reshape(y1 - y0, SS, x1 - x0, SS).mean((1, 3))
    # feathered leg mask
    legm = ndimage.gaussian_filter(ndimage.binary_dilation(sub, iterations=2).astype(np.float32), 0.9)
    alpha = np.clip(ndimage.gaussian_filter(cover, 0.6) * legm, 0, 1)
    # shading from the fur's own light, plus cylinder falloff
    L = lum[y0:y1, x0:x1]
    Lref = np.median(L[sub]) if sub.any() else L.mean()
    shade = np.clip(L / Lref, 0.55, 1.4)
    shade = ndimage.gaussian_filter(shade, 2.0)
    ux = np.clip((np.arange(x0, x1) - xm) / hw, -1, 1)
    cyl = 0.50 + 0.50 * np.clip(1 - ux ** 2, 0, 1) ** 0.35
    cyl = cyl * (1.0 + 0.10 * np.clip(-ux, 0, 1))  # key light from the viewer's left
    col = BAND[None, None, :] * (shade * cyl[None, :])[..., None]
    # a soft lighter rim along the top edge, darker along the bottom
    ycr = (yc0 - arc * (1 - ux ** 2))[None, :]
    yr = np.arange(y0, y1)[:, None] + 0.5
    top = np.exp(-((yr - (ycr - bh / 2 + 2.5)) ** 2) / 4.0)
    bot = np.exp(-((yr - (ycr + bh / 2 - 2.0)) ** 2) / 4.0)
    col = col * (1 + 0.22 * top[..., None]) * (1 - 0.25 * bot[..., None])
    rng = np.random.default_rng(7)
    weave = ndimage.gaussian_filter(rng.normal(0, 1, col.shape[:2]), (0.5, 2.5))
    col = col * (1 + 0.05 * weave[..., None])
    col = np.clip(col, 0, 255)
    reg = out_a[y0:y1, x0:x1]
    # contact shadow on the fur just above and below the band
    ao = (np.exp(-((yr - (ycr - bh / 2)) ** 2) / 10.0) + np.exp(-((yr - (ycr + bh / 2 + 1)) ** 2) / 14.0)) * legm
    reg *= (1 - 0.22 * np.clip(ao, 0, 1))[..., None]
    reg[:] = reg * (1 - alpha[..., None]) + col * alpha[..., None]
    out_a[y0:y1, x0:x1] = reg
    # stud: rounded red-orange block with a silver-lavender ring, on the band's front
    sx = xm + sdx * hw
    sy = yc0 - arc
    sw, sh = 30, 24
    big = Image.new("RGBA", ((sw + 12) * SS, (sh + 12) * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    o = 6 * SS
    d.rounded_rectangle([o + SS, o + 3 * SS, o + sw * SS + SS, o + sh * SS + 3 * SS], radius=8 * SS, fill=(40, 8, 10, 90))  # contact shadow
    d.rounded_rectangle([o, o, o + sw * SS, o + sh * SS], radius=8 * SS, fill=(150, 36, 32, 255))
    # vertical and diagonal shading built up in bands (light from the upper left)
    for i in range(12):
        t = i / 11
        c = tuple(int(v) for v in (np.array([234, 96, 70]) * (1 - t) + np.array([176, 44, 38]) * t))
        inset = (1 + i * 0.25) * SS
        d.rounded_rectangle([o + inset, o + inset + i * SS * 0.6, o + sw * SS - inset, o + sh * SS - inset], radius=7 * SS, fill=c + (255,))
    d.ellipse([o + 4 * SS, o + 2.5 * SS, o + 13 * SS, o + 7 * SS], fill=(255, 190, 170, 150))  # soft specular
    cx, cy = o + sw * SS / 2, o + sh * SS / 2 + SS
    d.ellipse([cx - 7.5 * SS, cy - 5.5 * SS, cx + 7.5 * SS, cy + 5.5 * SS], fill=(120, 70, 86, 255))
    d.ellipse([cx - 6.5 * SS, cy - 5 * SS, cx + 6.5 * SS, cy + 4.5 * SS], fill=(214, 200, 214, 255))
    d.ellipse([cx - 6 * SS, cy - 4.8 * SS, cx + 4 * SS, cy + 1 * SS], fill=(246, 238, 246, 255))
    d.ellipse([cx - 3 * SS, cy - 2.2 * SS, cx + 3 * SS, cy + 2.2 * SS], fill=(178, 70, 80, 255))
    stud = big.resize((sw + 12, sh + 12), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.5))
    # match the stud to the local light
    lx = int(round(sx)); ly = int(round(sy))
    k = float(np.clip(lum[ly - 12:ly + 12, lx - 15:lx + 15].mean() / Lref, 0.7, 1.25))
    sa = np.asarray(stud).astype(np.float32)
    sa[..., :3] = np.clip(sa[..., :3] * (0.85 + 0.15 * k), 0, 255)
    px, py = int(round(sx - (sw + 12) / 2)), int(round(sy - (sh + 12) / 2))
    reg = out_a[py:py + sh + 12, px:px + sw + 12]
    al = sa[..., 3:4] / 255.0
    reg[:] = reg * (1 - al) + sa[..., :3] * al
    print("leg x %d-%d centre %.0f half-width %.0f band y %d stud (%d,%d)" % (lx0, lx1, xm, hw, yc0, sx, sy))

res = Image.fromarray(np.clip(out_a, 0, 255).astype(np.uint8))
res.save(out)
if len(sys.argv) > 3:
    c = res.crop((760, 1000, 1120, 1320))
    c.resize((c.width * 3, c.height * 3), Image.LANCZOS).save(sys.argv[3])
