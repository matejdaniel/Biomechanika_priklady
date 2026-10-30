"""008 – Maximální síla svalu: ilustrace z Gemini (008_pruznost_max_sila_svalu_ilustrace.png) + popisky.
Izometrický cvik extenze kolene (bérec připoutaný popruhem), čtyřhlavý sval a jeho příčný řez (PCSA)."""
from styl import *
from PIL import Image
import numpy as np

ILU = '008_pruznost_max_sila_svalu_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy(); ilu[ilu.min(2) > 235] = 255
H, W, _ = ilu.shape
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(150, W - 20); ax.set_ylim(H - 140, 0)

# čtyřhlavý sval a jeho síla
ax.plot([1000, 1060], [720, 430], color=INK, lw=1)
ax.text(1080, 420, 'čtyřhlavý sval\nstehenní', fontsize=15, ha='center', va='bottom', linespacing=1.0)
sila(ax, 1300, 610, 980, 610); ax.patches[-1].set_zorder(6)
ax.text(1310, 610, '$F$ = ?', color=SILA, fontsize=18, va='center')
# průřez
ax.text(2085, 270, 'příčný řez svalem', fontsize=16, ha='center', va='bottom')
ax.text(2085, 1000, 'PCSA = 2750 mm²', color=ROZMER, fontsize=18, ha='center', va='top')
ax.text(2085, 1110, 'σ = 1 MPa', fontsize=18, ha='center', va='top')
# popruh – izometrie
ax.plot([1350, 1560], [1150, 1290], color=INK, lw=1)
ax.text(1570, 1290, 'popruh: bérec se nemůže\npohnout → izometrická\nkontrakce', fontsize=14, va='top', linespacing=1.0)
uloz(fig, '008_pruznost_max_sila_svalu.png')
