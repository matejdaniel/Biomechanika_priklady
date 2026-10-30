"""017 – Napětí v tibii: ilustrace z Gemini (017_pruznost_tibie_ilustrace.png) + síly, kóty a data (podle předlohy)."""
from styl import *
from PIL import Image
import numpy as np

ILU = '017_pruznost_tibie_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy(); ilu[ilu.min(2) > 235] = 255
H, W, _ = ilu.shape
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(60, 2330); ax.set_ylim(1850, -280)
F = dict(fontsize=16, color=SILA, va='center')
# --- noha: síly
sila(ax, 577, -200, 577, 90); ax.text(620, -150, '750 N', **F)                  # tíha těla na koleno
sila(ax, 345, 1190, 345, 800); ax.text(330, 1000, '2050 N', ha='right', **{k: v for k, v in F.items()})  # tah lýtkového svalu za patu
sila(ax, 820, 1760, 820, 1500); ax.text(865, 1700, '750 N', **F)                # reakce podložky pod prsty
ax.text(330, 1100, '(lýtkový sval)', fontsize=12, ha='right', va='center', color=SILA)
# --- izolovaná tibie
sila(ax, 1365, -230, 1365, 240); ax.text(1410, -170, '2800 N', **F)
sila(ax, 1390, 1800, 1390, 1395); ax.text(1435, 1740, '2800 N', **F)
for y in (254, 1382): ax.plot([1140, 1300], [y, y], color=ROZMER, lw=1, ls=':')
kota(ax, 1170, 254, 1170, 1382, '', dy=0)
ax.text(1140, 818, '0,40 m', color=ROZMER, fontsize=16, ha='right', va='center')
# --- průřez
cx, cy, R, r = 2035, 848, 145, 92
for x in (cx - R, cx + R): ax.plot([x, x], [cy, cy + R + 90], color=ROZMER, lw=1, ls=':')
kota(ax, cx - R, cy + R + 70, cx + R, cy + R + 70, '', dy=0)
ax.text(cx, cy + R + 150, '2,5 cm', color=ROZMER, fontsize=16, ha='center', va='center')
for x in (cx - r, cx + r): ax.plot([x, x], [cy - r - 110, cy], color=ROZMER, lw=1, ls=':')
kota(ax, cx - r, cy - R - 60, cx + r, cy - R - 60, '', dy=0)
ax.text(cx, cy - R - 140, '1,3 cm', color=ROZMER, fontsize=16, ha='center', va='center')
ax.text(cx, cy - R - 260, 'průřez tibie', fontsize=16, ha='center', va='center')
ax.text(cx, cy + R + 330, 'σ = ?', color=ROZMER, fontsize=22, ha='center', va='center')
uloz(fig, '017_pruznost_tibie.png')
