"""012 – Youngův modul v bodech diagramu: tahový diagram oceli (s mezí kluzu) + motiv kostního šroubu z oceli."""
from styl import *
import numpy as np
from scipy.interpolate import PchipInterpolator as Pchip
from matplotlib.patches import Polygon, FancyBboxPatch
from pp_grafy1 import kval

def sroub(ax):
    """Kortikální kostní šroub (vodorovně): hlava se zápustem, závitová část a hrot."""
    ax.set_xlim(-.4, 6.2); ax.set_ylim(-1.4, 1.6); ax.axis('off'); ax.set_aspect('equal')
    OC, TM = '#b8c4cf', '#6d7a86'
    ax.add_patch(FancyBboxPatch((0, -.7), .6, 1.4, boxstyle='round,pad=0,rounding_size=.25', fc=OC, ec=INK, lw=1.6, zorder=3))
    ax.plot([.18, .18], [-.35, .35], color=TM, lw=3, zorder=4); ax.plot([.42, .42], [-.35, .35], color=TM, lw=3, zorder=4)
    ax.add_patch(Polygon([(.6, -.3), (5.0, -.3), (5.8, 0), (5.0, .3), (.6, .3)], closed=True, fc=OC, ec=INK, lw=1.6, zorder=2))
    for x in np.arange(.85, 5.2, .32):                       # závity
        ax.plot([x, x + .16], [.3, .52], color=INK, lw=1.4, zorder=3); ax.plot([x + .16, x + .32], [.52, .3], color=INK, lw=1.4, zorder=3)
        ax.plot([x, x + .16], [-.3, -.52], color=INK, lw=1.4, zorder=3); ax.plot([x + .16, x + .32], [-.52, -.3], color=INK, lw=1.4, zorder=3)
    ax.text(2.9, .85, 'ocelový šroub do kosti', fontsize=13, ha='center', va='bottom')

ILU = '012_pruznost_body_diagramu_ilustrace.png'

def dlaha(ax):
    from PIL import Image
    im = Image.open(ILU).convert('RGB'); a = np.asarray(im)
    ys, xs = np.where(a.min(2) < 225)
    k = np.asarray(im.crop((xs.min() - 10, ys.min() - 10, xs.max() + 10, ys.max() + 10))).copy()
    k[k.min(2) > 235] = 255
    ax.imshow(k); ax.axis('off')
    ax.text(k.shape[1] / 2, -40, 'ocelová dlaha a šrouby na zlomené kosti', fontsize=13, ha='center', va='bottom')

if __name__ == '__main__':
    fig, ax = start(6, 4, osy=True)
    xs, ys = [.05, .14, .3, .55, .7, 1], [3.6, 3.45, 3.85, 4.75, 4.85, 4.1]
    x = np.linspace(.05, 1, 300)
    ax.plot([0, .05], [0, 3.6], color=SILA); ax.plot(x, Pchip(xs, ys)(x), color=SILA)
    for (xi, t) in [(.14, 'A'), (.62, 'B')]:
        yi = Pchip(xs, ys)(xi)
        ax.plot(xi, yi, 'o', color=INK, ms=8); ax.text(xi - .02, yi + .35, t, fontsize=22)
    ax.set_xlim(0, 1.08); ax.set_ylim(0, 5.8)
    kval(ax, 'poměrná deformace ε', 'napětí σ')
    ins = ax.inset_axes([0.38, 0.03, 0.6, 0.36]); dlaha(ins)
    uloz(fig, '012_pruznost_body_diagramu.png')
