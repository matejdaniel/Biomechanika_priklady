"""002 – Porušení kolagenních vláken: tahový diagram šlachy s úseky I–III + motiv lýtka a Achillovy šlachy."""
from styl import *
import numpy as np
from scipy.interpolate import PchipInterpolator as Pchip
from pp_grafy1 import kval
from importlib import import_module
motiv = import_module("001_pruznost_modul_slachy").motiv

fig, ax = start(6, 4, osy=True)
xs, ys = [0, 2, 3.2, 5.5, 7.5, 10], [0, .4, 1.4, 3.6, 4.6, 5]
x = np.linspace(0, 10, 300); ax.plot(x, Pchip(xs, ys)(x), color=SILA)
for xi in (2.6, 6.4): ax.axvline(xi, color=ROZMER, lw=1.2, ls='--', alpha=.6)
for (xc, t) in [(1.3, 'I'), (4.5, 'II'), (8.2, 'III')]:
    ax.text(xc, 5.7, t, color=ROZMER, fontsize=22, ha='center', fontfamily='DejaVu Serif')
ax.set_xlim(0, 10.6); ax.set_ylim(0, 6.3)
kval(ax, 'prodloužení šlachy', 'síla ve šlaše')
ins = ax.inset_axes([0.63, 0.03, 0.37, 0.52]); motiv(ins)
uloz(fig, '002_pruznost_poruseni_vlaken.png')
