"""005 – Kočár pro Popelku: ilustrace z Gemini + kóty a hmotnosti."""
from styl import *
from PIL import Image
import numpy as np

ILU = '005_skalovani_popelka_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy()
ilu[ilu.min(2) > 235] = 255
H, W, _ = ilu.shape
# změřené okraje: dýně x 317–748, kočár x 1119–2366, země y ≈ 1415
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(150, 2500); ax.set_ylim(1700, 110)
y_k = 1520
for x in (317, 748, 1119, 2366):
    ax.plot([x, x], [1440, y_k + 25], color=ROZMER, lw=1.2, alpha=.6)
kota(ax, 317, y_k, 748, y_k, '', dy=0);  ax.text(532, y_k + 85, '30 cm', color=ROZMER, fontsize=22, ha='center', va='center')
kota(ax, 1119, y_k, 2366, y_k, '', dy=0); ax.text(1742, y_k + 85, '3 m', color=ROZMER, fontsize=22, ha='center', va='center')
ax.text(532, 960, '4 kg', fontsize=22, ha='center', va='center')
ax.text(1700, 200, '? kg', fontsize=22, ha='center', va='center')
uloz(fig, '005_skalovani_popelka.png')
