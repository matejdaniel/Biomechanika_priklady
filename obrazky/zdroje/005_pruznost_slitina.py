"""005 – Youngův modul nové slitiny: tahový diagram + motiv implantátu (kostní dlaha se šrouby na zlomené kosti)."""
from styl import *
import numpy as np
from scipy.interpolate import PchipInterpolator as Pchip
from matplotlib.patches import FancyBboxPatch, Circle
from importlib import import_module
dlouha_kost = import_module("003_pruznost_deformace_kosti").dlouha_kost

def implantat(ax):
    ax.set_xlim(-.4, 5.8); ax.set_ylim(-1.4, 1.5); ax.axis('off'); ax.set_aspect('equal')
    dlouha_kost(ax, 0, 5.4, 0, .28)
    ax.plot([2.55, 2.75, 2.65, 2.85], [-.3, -.05, .08, .3], color=INK, lw=1.6, zorder=4)          # lomná linie
    ax.add_patch(FancyBboxPatch((1.3, .2), 2.8, .22, boxstyle='round,pad=0.02', fc='#b8c4cf', ec=INK, lw=1.6, zorder=5))
    for x in (1.55, 2.05, 3.35, 3.85):
        ax.add_patch(Circle((x, .31), .07, fc='#6d7a86', ec=INK, lw=1, zorder=6))
    ax.text(2.7, .62, 'dlaha z nové slitiny', fontsize=13, ha='center', va='bottom')

fig, ax = start(6, 4, osy=True)
x = np.linspace(0, 0.035, 300)
ax.plot(x, Pchip([0, .01, .013, .02, .028, .035], [0, 2.0, 2.35, 2.65, 2.8, 2.85])(x), color=SILA)
ax.set_xlim(0, .036); ax.set_ylim(0, 3.6)
ax.set_xticks([0, .01, .02, .03]); ax.set_xticklabels(['0', '0,01', '0,02', '0,03']); ax.set_yticks([0, 1, 2, 3])
ax.set_xticks(np.arange(0, .036, .0025), minor=True); ax.set_yticks(np.arange(0, 3.6, .25), minor=True)
ax.grid(True, which='major', alpha=.35, lw=.9, color='#999999'); ax.grid(True, which='minor', alpha=.2, lw=.6, color='#999999')
for s in ('top', 'right'): ax.spines[s].set_visible(False)
ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [kPa]')
ins = ax.inset_axes([0.42, 0.05, 0.56, 0.48]); ins.set_facecolor('white'); implantat(ins)
ins.set_axis_on(); ins.set_xticks([]); ins.set_yticks([])
for sp in ins.spines.values(): sp.set_edgecolor('#aaaaaa'); sp.set_linewidth(1)
uloz(fig, '005_pruznost_slitina.png')
