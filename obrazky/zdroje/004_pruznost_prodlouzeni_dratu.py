"""004 – Prodloužení lanka trakce: ilustrace z Gemini (004_pruznost_prodlouzeni_dratu_ilustrace.png) + popisky."""
from styl import *
from PIL import Image
import numpy as np

ILU = '004_pruznost_prodlouzeni_dratu_ilustrace.png'
ilu = np.asarray(Image.open(ILU).convert('RGB')).copy(); ilu[ilu.min(2) > 235] = 255
H, W, _ = ilu.shape
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(150, W + 520); ax.set_ylim(H - 150, 250)
# síla od závaží
sila(ax, 2228, 1000, 2228, 1280, '$F$ = 115 N', dx=50, dy=-10)
# lanko trakce: popisek s údaji
ax.plot([2240, 2400], [560, 470], color=INK, lw=1)
for i, (t, c, fs) in enumerate([('ocelové lanko trakce', INK, 17), ('$L$ = 1,12 m', ROZMER, 16),
                                ('$S$ = 6,0·10$^{-3}$ cm²', INK, 15), ('$E$ = 20·10$^{10}$ N/m²', INK, 15),
                                (r'$\Delta l$ = ?', ROZMER, 18)]):
    ax.text(2410, 470 + i * 110, t, fontsize=fs, va='center', color=c)
# Kirschnerův drát
ax.plot([1640, 1330], [745, 560], color=INK, lw=1)
ax.text(1330, 545, 'Kirschnerův drát', fontsize=15, ha='center', va='bottom')
uloz(fig, '004_pruznost_prodlouzeni_dratu.png')
