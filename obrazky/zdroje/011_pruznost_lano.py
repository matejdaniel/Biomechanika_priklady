"""011 – Bezpečnostní lano: ilustrace z Gemini (011_pruznost_lano_ilustrace.png) + kóty a data."""
from styl import *
from PIL import Image
import numpy as np

ILU = '011_pruznost_lano_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy(); ilu[ilu.min(2) > 235] = 255
H, W, _ = ilu.shape
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(350, W - 250); ax.set_ylim(H - 40, 20)
TOP, KON = 400, 1100                      # úchyt lana a místo připojení k postroji
K1 = TOP + (KON - TOP) * 200 / 205        # konec nezatíženého lana
# kóty délek lana
for y in (TOP, K1): ax.plot([830, 1170], [y, y], color=ROZMER, lw=1, ls=':')
ax.plot([1230, 1660], [KON, KON], color=ROZMER, lw=1, ls=':'); ax.plot([1230, 1660], [TOP, TOP], color=ROZMER, lw=1, ls=':')
kota(ax, 870, TOP, 870, K1, '', dy=0)
ax.text(840, (TOP + K1) / 2, '$l_1$ = 200 cm', color=ROZMER, fontsize=17, ha='right', va='center')
ax.text(840, (TOP + K1) / 2 + 85, '(bez zátěže)', color=ROZMER, fontsize=13, ha='right', va='center')
kota(ax, 1620, TOP, 1620, KON, '', dy=0)
ax.text(1650, (TOP + KON) / 2, '$l_2$ = 205 cm', color=ROZMER, fontsize=17, ha='left', va='center')
ax.text(1650, (TOP + KON) / 2 + 85, '(s dělníkem)', color=ROZMER, fontsize=13, ha='left', va='center')
# tíha dělníka
sila(ax, 1160, 1250, 1160, 1600); ax.patches[-1].set_zorder(6)
ax.text(1020, 1560, '$G$ = 1500 N', color=SILA, fontsize=18, ha='right', va='center')
# data lana
ax.text(1700, 1250, '$S$ = 100 mm²', fontsize=17, va='center')
ax.text(1700, 1390, '$E$ = ?', color=ROZMER, fontsize=22, va='center')
uloz(fig, '011_pruznost_lano.png')
