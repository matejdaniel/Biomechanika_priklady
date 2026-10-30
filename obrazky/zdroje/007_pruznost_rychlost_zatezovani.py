"""007 – Rychlost zatěžování kosti: tahové křivky A–D + motiv trhacího stroje se vzorkem kosti."""
from styl import *
import numpy as np
from scipy.interpolate import PchipInterpolator as Pchip
from matplotlib.patches import Rectangle, FancyBboxPatch
from pp_grafy1 import kval

def stroj(ax):
    """Trhací stroj: rám, horní a dolní čelisti, mezi nimi vzorek kosti, tah silou F."""
    ax.set_xlim(-4.6, 2.2); ax.set_ylim(-3.6, 3.6); ax.axis('off'); ax.set_aspect('equal')
    ax.add_patch(Rectangle((-1.9, 2.6), 3.8, .45, fc='#b8c4cf', ec=INK, lw=1.6))              # příčník
    ax.add_patch(Rectangle((-1.9, -3.2), 3.8, .45, fc='#b8c4cf', ec=INK, lw=1.6))             # základna
    for x in (-1.75, 1.6): ax.add_patch(Rectangle((x, -2.75), .15, 5.35, fc='#d5dde4', ec=INK, lw=1.2))  # sloupy
    for y in (1.55, -2.0):                                                                  # čelisti
        ax.add_patch(FancyBboxPatch((-.45, y), .9, .55, boxstyle='round,pad=0.03', fc='#8d99a6', ec=INK, lw=1.4, zorder=4))
    ax.plot([0, 0], [2.1, 2.6], color=INK, lw=2); ax.plot([0, 0], [-2.0, -2.75], color=INK, lw=2)
    ax.add_patch(FancyBboxPatch((-.22, -1.45), .44, 3.0, boxstyle='round,pad=0,rounding_size=.12', fc='#ecdcb8', ec=INK, lw=1.6, zorder=3))
    sila(ax, .7, .7, .7, 1.7); sila(ax, .7, -.7, .7, -1.7)
    ax.text(1.0, 1.0, '$F$', color=SILA, fontsize=17); ax.text(1.0, -1.4, '$F$', color=SILA, fontsize=17)
    ax.text(0, 3.2, 'trhací stroj', fontsize=13, ha='center', va='bottom')
    ax.text(-2.15, 0, 'vzorek\nkosti', fontsize=13, ha='right', va='center', linespacing=1.0)
    ax.plot([-2.1, -.25], [0, 0], color=INK, lw=.9)

fig, ax = start(6, 4, osy=True)
C = {'A': (SILA, [0, .1, .2, .35], [0, 5.2, 6.6, 7.0]), 'B': (ROZMER, [0, .3, .5, .7], [0, 3.6, 5.6, 5.9]),
     'C': ('#f77f00', [0, .5, 1.0, 1.35], [0, 1.6, 2.9, 3.1]), 'D': (BOD, [0, .5, 1.0, 1.35], [0, 1.1, 1.9, 2.0])}
for k, (c, xs, ys) in C.items():
    x = np.linspace(0, xs[-1], 200); ax.plot(x, Pchip(xs, ys)(x), color=c)
    ax.text(xs[-1] + .04, ys[-1], k, color=c, fontsize=22, va='center')
ax.set_xlim(0, 1.6); ax.set_ylim(0, 7.8)
kval(ax, 'poměrné prodloužení ε', 'napětí σ')
ins = ax.inset_axes([0.5, 0.42, 0.5, 0.58]); stroj(ins)
uloz(fig, '007_pruznost_rychlost_zatezovani.png')
