"""019 – Poměrné prodloužení kosti: kost upnutá ke stěně před zatížením (čárkovaně) a po zatížení silou F."""
from styl import *
import numpy as np
from matplotlib.patches import Rectangle, Circle
from importlib import import_module
_m = import_module("003_pruznost_deformace_kosti"); dlouha_kost, KOST = _m.dlouha_kost, _m.KOST


if __name__ == '__main__':
    fig, ax = start(6, 4)
    r, L, dL = .2, 5.0, .35                   # Δl zvětšeno pro názornost
    # stěna
    ax.add_patch(Rectangle((-.35, -2.0), .35, 3.3, fc='#d9dcd6', ec=INK, lw=1.6))
    for y in np.linspace(-1.9, 1.1, 9): ax.plot([-.6, -.35], [y - .2, y], color=INK, lw=1.2)
    # kost před zatížením – jen čárkovaný obrys
    y1 = .55
    dlouha_kost(ax, 0, L, y1, r)
    for p in ax.patches[-2:]: p.set_facecolor('none'); p.set_linestyle('--'); p.set_edgecolor('#8a7a5a')
    ax.text(L / 2, y1 + .58, 'před zatížením', fontsize=15, ha='center', color='#6d6048')
    # kost po zatížení
    y2 = -1.0
    dlouha_kost(ax, 0, L + dL, y2, r)
    ax.text(L / 2, y2 - .75, 'po zatížení', fontsize=15, ha='center')
    sila(ax, L + dL + .05, y2, L + dL + 1.1, y2, '$F$ = 150 N', dx=-.9, dy=.25)
    # kóty
    for x in (L, L + dL): ax.plot([x, x], [y1 + .5, y2 - .8], color=ROZMER, lw=1, ls=':')
    kota(ax, 0, y1 + .95, L, y1 + .95, '', dy=0)
    ax.text(L / 2, y1 + 1.15, '$l_0$ = 100 mm', color=ROZMER, fontsize=17, ha='center')
    kota(ax, L, y2 - .7, L + dL, y2 - .7, '', dy=0)
    ax.text(L + dL + .15, y2 - .7, r'$\Delta l$ = 1 mm', color=ROZMER, fontsize=16, va='center')
    ax.text(L + dL + .15, y2 - 1.0, '(zvětšeno)', color=ROZMER, fontsize=12, va='center')
    # průřez
    cx, cy = 1.0, -2.35
    ax.add_patch(Circle((cx, cy), .28, fc=KOST, ec=INK, lw=1.8))
    kota(ax, cx - .28, cy, cx + .28, cy, '', dy=0)
    ax.text(cx + .45, cy, 'průřez kosti, $d$ = 1 cm', fontsize=15, va='center')
    ax.text(4.6, -2.35, r'$\varepsilon$ = ?', color=ROZMER, fontsize=22, va='center')
    ax.set_xlim(-.8, 7.0); ax.set_ylim(-2.8, 1.95)
    uloz(fig, '019_pruznost_prodlouzeni_kosti.png')
