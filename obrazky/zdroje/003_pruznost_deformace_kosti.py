"""003 – Deformace kosti v tahu: dlouhá kost (stylizovaná stehenní kost) tažená silami F, průřez d = 5 cm."""
from styl import *
import numpy as np
from matplotlib.patches import Circle
from importlib import import_module
tvar = import_module("001_pruznost_modul_slachy").tvar

KOST = '#ecdcb8'

def dlouha_kost(ax, x0, x1, y, r):
    """Dlouhá kost: štíhlá válcová diafýza a rozšířené kloubní konce (epifýzy)."""
    L = x1 - x0
    e = .09 * L                                    # délka epifýzy
    obrys = [(x0 + .02 * L, y + 1.9 * r), (x0 + .5 * e, y + 2.4 * r), (x0 + e, y + 2.0 * r), (x0 + 1.6 * e, y + 1.1 * r),
             (x0 + 2.2 * e, y + r), (x0 + .5 * L, y + .95 * r), (x1 - 2.2 * e, y + r), (x1 - 1.6 * e, y + 1.1 * r),
             (x1 - e, y + 2.0 * r), (x1 - .5 * e, y + 2.5 * r), (x1 - .02 * L, y + 1.8 * r), (x1, y + .2 * r),
             (x1 - .02 * L, y - 1.7 * r), (x1 - .5 * e, y - 2.4 * r), (x1 - e, y - 2.0 * r), (x1 - 1.6 * e, y - 1.1 * r),
             (x1 - 2.2 * e, y - r), (x0 + .5 * L, y - .95 * r), (x0 + 2.2 * e, y - r), (x0 + 1.6 * e, y - 1.1 * r),
             (x0 + e, y - 2.0 * r), (x0 + .5 * e, y - 2.5 * r), (x0 + .02 * L, y - 1.8 * r), (x0, y - .1 * r)]
    tvar(ax, obrys, fc=KOST, ec=INK, lw=2.2, zorder=2)
    # dřeňová dutina v diafýze (zaoblený obdélník)
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x0 + 2.4 * e, y - .4 * r), L - 4.8 * e, .8 * r, boxstyle='round,pad=0,rounding_size=%g' % (.4 * r),
                                fc='#f7efdc', ec='#c4ab78', lw=1, zorder=3))

if __name__ == '__main__':
    fig, ax = start(6, 2.6)
    r = .2
    dlouha_kost(ax, 0, 5.4, 0, r)
    sila(ax, 0, 0, -1.0, 0, '$F$', dx=-.05, dy=.15)
    sila(ax, 5.4, 0, 6.4, 0, '$F$ = 100 N', dx=-.75, dy=.15)
    # průřez diafýzou
    cx, cy = 2.7, -1.05
    R = 1.6 * r
    ax.plot([2.7, 2.7], [-r, cy + R], color=ROZMER, lw=1, ls=':')
    ax.add_patch(Circle((cx, cy), 1.6 * r, fc=KOST, ec=INK, lw=2, zorder=3))
    kota(ax, cx - R, cy - R - .15, cx + R, cy - R - .15, '', dy=0)
    ax.text(cx + R + .15, cy, '$d$ = 5 cm', color=ROZMER, fontsize=18, va='center')
    ax.text(cx - R - .15, cy, 'průřez', fontsize=16, ha='right', va='center')
    ax.text(2.7, .8, '$E$ = 10 GPa', fontsize=20, ha='center')
    ax.set_xlim(-1.4, 6.8); ax.set_ylim(-1.7, 1.05)
    uloz(fig, '003_pruznost_deformace_kosti.png')
