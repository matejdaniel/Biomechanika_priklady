"""006 – Tuhost bicepsu koně: graf síla–prodloužení + ilustrace koně z Gemini (006_pruznost_biceps_kone_ilustrace.png)."""
from styl import *
import numpy as np
from PIL import Image
from scipy.interpolate import PchipInterpolator as Pchip

ILU = '006_pruznost_biceps_kone_ilustrace.png'
im = Image.open(ILU).convert('RGB'); a = np.asarray(im)
m = a.min(2) < 225; ys, xs = np.where(m)
x0, x1, y0, y1 = xs.min() - 20, xs.max() + 20, ys.min() - 20, ys.max() + 20
kun = np.asarray(im.crop((x0, y0, x1, y1))).copy(); kun[kun.min(2) > 235] = 255

fig, ax = start(6, 4, osy=True)
x1_ = np.linspace(0, 18.8, 200); ax.plot(x1_, Pchip([0, 5, 10, 15, 17.5, 18.8], [0, 2, 4, 6.3, 8.6, 11.5])(x1_), color=SILA)
x2_ = np.linspace(0, 17.5, 200); ax.plot(x2_, Pchip([0, 5, 10, 15, 17.5], [0, 2, 4, 6, 7.0])(x2_), color=ROZMER)
ax.plot([17.5, 17.2], [7.0, 6.2], color=ROZMER)
ax.text(11.2, 10.2, 'in vivo', color=SILA, fontsize=20)
ax.text(11.2, 9.45, '(měřeno v živém koni)', color=SILA, fontsize=14)
ax.text(13.2, 3.9, 'in vitro', color=ROZMER, fontsize=20)
ax.text(13.2, 3.45, '(vypreparovaný sval\nv laboratoři)', color=ROZMER, fontsize=14, va='top', linespacing=1.0)
ax.set_xlim(0, 21); ax.set_ylim(0, 12.5)
ax.set_xticks(range(0, 21, 5)); ax.set_yticks(range(0, 13, 2))
graf(ax); ax.set_xlabel('prodloužení [mm]'); ax.set_ylabel('síla [kN]')
ins = ax.inset_axes([0.03, 0.5, 0.42, 0.5]); ins.imshow(kun); ins.axis('off')
# popisek svalu (souřadnice v pixelech výřezu)
bx, by = 1290 - x0, 1050 - y0
ins.annotate('biceps', xy=(bx, by), xytext=(bx + 650, by + 350), fontsize=15,
             arrowprops=dict(arrowstyle='-', color=INK, lw=1), color=SILA, ha='left')
uloz(fig, '006_pruznost_biceps_kone.png')
