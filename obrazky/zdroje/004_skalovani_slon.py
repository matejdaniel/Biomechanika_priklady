"""004 – Slon a mládě: ilustrace z Gemini + kóty délky a hmotnosti."""
from styl import *
from PIL import Image
import numpy as np

ILU = '004_skalovani_slon_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy()
ilu[ilu.min(2) > 235] = 255          # sjednocení téměř bílého pozadí na čistě bílou
H, W, _ = ilu.shape
# změřené okraje (kontura) – mládě x 360–923, dospělý x 1256–2359, země y ≈ 1270
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(220, 2470); ax.set_ylim(1620, 120)
y_k = 1360
for x in (360, 923, 1256, 2359):
    ax.plot([x, x], [1290, y_k + 25], color=ROZMER, lw=1.2, alpha=.6)
kota(ax, 360, y_k, 923, y_k, '', dy=0); ax.text(641, y_k + 100, 'L/2', color=ROZMER, fontsize=24, fontfamily='DejaVu Sans', fontstyle='italic', ha='center', va='center')
kota(ax, 1256, y_k, 2359, y_k, '', dy=0); ax.text(1807, y_k + 100, 'L', color=ROZMER, fontsize=24, fontfamily='DejaVu Sans', fontstyle='italic', ha='center', va='center')
ax.text(641, 760, '? kg', fontsize=22, ha='center', va='center')
ax.text(1807, 330, '4500 kg', fontsize=22, ha='center', va='center')
uloz(fig, '004_skalovani_slon.png')
