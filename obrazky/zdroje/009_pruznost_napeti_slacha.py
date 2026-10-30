"""009 – Napětí ve šlaše: ilustrace z Gemini (009_pruznost_napeti_slacha_ilustrace.png) + popisky a data."""
from styl import *
from PIL import Image
import numpy as np

ILU = '009_pruznost_napeti_slacha_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy(); ilu[ilu.min(2) > 235] = 255
H, W, _ = ilu.shape
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(150, W - 150); ax.set_ylim(H + 230, -260)
# tahové síly
sila(ax, 737, 60, 737, -220); ax.text(800, -150, '$F$ = 2 kN', color=SILA, fontsize=19, va='center')
sila(ax, 760, 1590, 760, 1880); ax.text(820, 1820, '$F$', color=SILA, fontsize=19, va='center')
# popisky částí
for (t, xt, yt, xb, yb) in [('sval', 380, 450, 590, 450), ('šlacha', 380, 1000, 690, 1000), ('kost', 380, 1500, 560, 1450)]:
    ax.text(xt, yt, t, fontsize=17, ha='right', va='center')
    ax.plot([xt + 15, xb], [yt, yb], color=INK, lw=1)
# průřez
ax.text(1700, 1230, 'průřez šlachy', fontsize=17, ha='center', va='top')
ax.text(1700, 1390, '$S$ = 80 mm²', color=ROZMER, fontsize=19, ha='center', va='top')
ax.text(1700, 1580, 'σ = ?', color=ROZMER, fontsize=24, ha='center', va='top')
uloz(fig, '009_pruznost_napeti_slacha.png')
