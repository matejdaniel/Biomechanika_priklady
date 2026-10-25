"""006 – Bronzová socha: ilustrace z Gemini + měřítko a hmotnosti. Model a socha v měřítku 1 : 20
(v obrázku pochopitelně nejsou nakresleny ve skutečném poměru)."""
from styl import *
from PIL import Image
from matplotlib.patches import FancyArrowPatch
import numpy as np

ILU = '006_skalovani_socha_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy()
ilu[ilu.min(2) > 235] = 255
H, W, _ = ilu.shape
# změřené okraje: model y 923–1592, socha y 72–1615
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(250, 2350); ax.set_ylim(1700, -200)
ax.text(602, 820, '5 kg', fontsize=22, ha='center', va='center')
ax.text(1720, -40, '? kg', fontsize=22, ha='center', va='center')
ax.add_patch(FancyArrowPatch((820, 1150), (1380, 1150), arrowstyle='-|>', mutation_scale=22, lw=3, color='#888888'))
ax.text(1100, 1060, 'měřítko 1 : 20', fontsize=20, ha='center', va='center')
uloz(fig, '006_skalovani_socha.png')
