"""010 – Napětí v Achillově šlaše: ilustrace (010_pruznost_napeti_achilova_ilustrace.png) + popisky a data."""
from styl import *
from PIL import Image
import numpy as np

ILU = '010_pruznost_napeti_achilova_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy(); ilu[ilu.min(2) > 235] = 255
H, W, _ = ilu.shape
fig, ax = start(6, 3.6)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(250, W - 50); ax.set_ylim(H - 30, -20)
# síla ve šlaše (míří podél šlachy k lýtkovému svalu)
sila(ax, 1500, 640, 1330, 230); ax.text(1430, 130, '$F$ = 2200 N', color=SILA, fontsize=18, ha='left', va='center')
# popis šlachy
ax.plot([1440, 1600], [760, 1180], color=INK, lw=1)
ax.text(1600, 1200, 'Achillova šlacha', fontsize=16, ha='center', va='top')
# průřez
ax.text(2235, 900, 'průřez šlachy', fontsize=16, ha='center', va='top')
ax.text(2235, 1030, '$S$ = 93 mm²', color=ROZMER, fontsize=18, ha='center', va='top')
ax.text(2235, 1190, 'σ = ?', color=ROZMER, fontsize=23, ha='center', va='top')
uloz(fig, '010_pruznost_napeti_achilova.png')
