"""015 – Youngův modul vazu: tahová zkouška vazu (015_pruznost_modul_vazu_ilustrace.png) + kóty a data."""
from styl import *
from PIL import Image
import numpy as np

ILU = '015_pruznost_modul_vazu_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy(); ilu[ilu.min(2) > 235] = 255
H, W, _ = ilu.shape
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(300, W - 200); ax.set_ylim(H + 220, -260)
A, B = 612, 1100                               # začátek a konec volné části vazu (mezi kostními bloky)
for y in (A, B): ax.plot([1000, 1215], [y, y], color=ROZMER, lw=1, ls=':')
kota(ax, 1050, A, 1050, B, '', dy=0)
ax.text(780, (A + B) / 2, '$l$ = 5 cm', color=ROZMER, fontsize=18, ha='right', va='center')
ax.plot([790, 1040], [(A + B) / 2, (A + B) / 2], color=ROZMER, lw=1)
# síly
sila(ax, 1263, 140, 1263, -200); ax.text(1330, -110, '$F$ = 100 N', color=SILA, fontsize=18, va='center')
sila(ax, 1263, 1540, 1263, 1880); ax.text(1330, 1790, '$F$', color=SILA, fontsize=18, va='center')
# popis a data
ax.plot([1320, 1760], [850, 700], color=INK, lw=1); ax.text(1770, 690, 'vaz', fontsize=17, va='center')
ax.text(1770, 930, '$S$ = 1 cm²', fontsize=17, va='center')
ax.text(1770, 1110, r'$\Delta l$ = 1 mm', color=ROZMER, fontsize=17, va='center')
ax.text(1770, 1300, '$E$ = ?', color=ROZMER, fontsize=22, va='center')
uloz(fig, '015_pruznost_modul_vazu.png')
