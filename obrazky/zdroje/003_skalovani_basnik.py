"""003 – Básník trpaslíkem: ilustrace z Gemini + kóty.
Malý básník je izometricky zmenšenou kopií velkého (výšky v poměru 1,0 : 1,5)."""
from styl import *
from PIL import Image
import numpy as np

ILU = '003_skalovani_basnik_ilustrace.png'
a = np.asarray(Image.open(ILU).convert('RGB')).astype(np.uint8)
H, W, _ = a.shape
# odstranění čáry země z Gemini (tenká vodorovná čára v y ≈ 1528–1545):
# pixel smaž, pokud je nad ním i pod ním (±10 px) světlé pozadí
a = a.copy(); g = a.astype(int).mean(2)
for y in range(1526, 1547):
    sv = (g[y - 10] > 200) & (g[y + 10] > 200)
    a[y, sv] = 255

def vyrez(x0, x1, y0, y1):
    sub = a[y0:y1, x0:x1]
    alfa = (np.abs(sub.astype(int) - 255).sum(2) > 45).astype(np.uint8) * 255
    # odstranění stínu a čáry země: ve spodní části ponech jen oblast bot
    # (šířka podle nohavic 160 px nad spodkem, rozšířená o 90 px na každou stranu)
    rad = sub.shape[0] - 160
    nohy = np.where(alfa[rad] > 0)[0]
    lo, hi = max(0, nohy.min() - 90), nohy.max() + 90
    for r in range(sub.shape[0] - 160, sub.shape[0]):
        alfa[r, :lo] = 0; alfa[r, hi:] = 0
        tmave = np.where(sub[r, lo:hi].mean(1) < 110)[0]
        if len(tmave) == 0: alfa[r] = 0; continue
        alfa[r, :lo + tmave.min()] = 0; alfa[r, lo + tmave.max() + 1:] = 0
    # vodorovné čáry země (dlouhé tmavé úseky v jednom řádku) odstraň
    for r in range(sub.shape[0] - 160, sub.shape[0]):
        if (sub[r].mean(1) < 150).sum() > 0.6 * sub.shape[1]: alfa[r] = 0
    return Image.fromarray(np.dstack([sub, alfa]), 'RGBA')

# velký: hlava y=117, boty y=1632; malý: hlava y=561, boty y=1604
velky = vyrez(1830, 2370, 100, 1636)
maly  = vyrez(1395, 1760, 545, 1608)
h_v = 1632 - 117
k = (h_v * 1.0 / 1.5) / (1604 - 561)
maly = maly.resize((round(maly.width * k), round(maly.height * k)), Image.LANCZOS)

ZEM = 1620
out = Image.new('RGBA', (W, H), (255, 255, 255, 255))
out.alpha_composite(velky, (1830, 100 + ZEM - 1632))
x_m = 1395 + round((365 - maly.width) / 2)
out.alpha_composite(maly, (x_m, ZEM - maly.height + 4))
ilu = np.asarray(out.convert('RGB'))

top_v = (2067, ZEM - h_v)
top_m = (x_m + (1550 - 1395) * k + (365 - 365 * k) / 2 * 0, ZEM - h_v / 1.5)
top_m = (1395 + (365 - maly.width) / 2 + (1550 - 1395) * k, ZEM - h_v / 1.5)
# bod O na zemi, ze kterého vychází přímka přes temena obou hlav
sl = (top_v[1] - top_m[1]) / (top_v[0] - top_m[0])
O = (top_v[0] - (top_v[1] - ZEM) / sl, ZEM)

fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(250, 2680); ax.set_ylim(1760, -160)
ax.plot([300, 2450], [ZEM, ZEM], color=INK, lw=1.4, alpha=.45)
# kóty podél přímky (posunuté kolmo nad přímku)
u = np.array([top_v[0] - O[0], top_v[1] - O[1]]); u = u / np.linalg.norm(u); n = np.array([u[1], -u[0]]) * 70
for (cil, txt, posun) in [(top_m, '1,0 m', 1.0), (top_v, '1,5 m', 3.0)]:
    p0 = np.array(O) + n * posun; p1 = np.array(cil) + n * posun
    kota(ax, *p0, *p1, '', dy=0)
    s = (p0 + p1) / 2 + n * .9
    ax.text(*s, txt, color=ROZMER, fontsize=21, ha='center', va='center',
            rotation=np.degrees(np.arctan2(-u[1], u[0])))
kota(ax, 2440, ZEM, 2440, top_v[1], '', dy=0)
ax.text(2480, (ZEM + top_v[1]) / 2, '1,8 m', color=ROZMER, fontsize=21, ha='left', va='center')
ax.text(2100, 1700, '80 kg', fontsize=21, ha='center', va='center')
ax.text(1565, 1700, '? kg', fontsize=21, ha='center', va='center')
uloz(fig, '003_skalovani_basnik.png')
