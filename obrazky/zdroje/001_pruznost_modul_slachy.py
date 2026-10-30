"""001 – Okamžitý modul pružnosti šlachy: tahový diagram šlachy + biomechanický motiv
(sval → šlacha → kost, šlacha napínaná silou F)."""
from styl import *
import numpy as np
from scipy.interpolate import PchipInterpolator as Pchip
from matplotlib.patches import Ellipse, Rectangle, FancyBboxPatch
from pp_grafy1 import kval
from styl import KUZE

def hladka(body, n=200):
    """Hladká uzavřená křivka procházející zadanými body (periodický spline)."""
    from scipy.interpolate import splprep, splev
    b = np.array(body + [body[0]])
    tck, _ = splprep([b[:, 0], b[:, 1]], s=0, per=True)
    return np.column_stack(splev(np.linspace(0, 1, n), tck))

def tvar(ax, body, **kw):
    from matplotlib.patches import Polygon
    p = Polygon(hladka(body), closed=True, **kw); p.set_sketch_params(.4, 120, 1); ax.add_patch(p); return p

def motiv(ax):
    """Bérec z boku: lýtkový sval přechází v Achillovu šlachu, která se upíná na patní kost."""
    ax.set_xlim(-2.8, 7.4); ax.set_ylim(-.4, 10.4); ax.axis('off'); ax.set_aspect('equal')
    # kůže: lýtko vzadu (vlevo) vyklenuté, vpředu holeň, dole noha s prsty vpravo
    tvar(ax, [(1.3, 10), (2.6, 10.1), (3.9, 10), (3.9, 8), (3.6, 5.5), (3.45, 3.2), (3.6, 2.2), (4.6, 1.5), (6.3, .85),
              (7.0, .4), (6.6, .05), (4.0, .05), (2.2, .08), (1.4, .4), (1.4, 1.3), (1.7, 2.6), (1.5, 4.2), (.8, 5.8),
              (.4, 7.5), (.6, 9.0)], fc=KUZE, ec=INK, lw=1.8, zorder=1)
    # lýtkový sval
    p = tvar(ax, [(1.0, 9.5), (2.0, 9.6), (2.45, 8.0), (2.3, 6.0), (2.0, 4.7), (1.7, 4.4), (1.15, 5.4), (.65, 6.9), (.6, 8.4)],
             fc=SVAL, ec=INK, lw=1.6, zorder=3)
    for k in np.linspace(.15, .85, 5):
        ln, = ax.plot([.6 + 1.85 * k, 1.75 + .2 * (k - .5)], [9.6, 4.4], color='white', lw=1.1, alpha=.85, zorder=4)
        ln.set_clip_path(p)
    # Achillova šlacha
    tvar(ax, [(1.68, 4.75), (2.05, 4.75), (2.0, 2.5), (2.05, 1.15), (1.75, 1.15), (1.72, 2.5)], fc='#f3e7d3', ec=INK, lw=1.3, zorder=3)
    ax.plot([1.88, 1.9], [4.6, 1.25], color='#c9b37a', lw=.9, zorder=4)
    # patní kost
    tvar(ax, [(1.6, 1.3), (2.6, 1.35), (3.0, .8), (2.6, .3), (1.7, .3), (1.5, .8)], fc='#f1e3c8', ec='#b9a273', lw=.9, zorder=2)
    sila(ax, -.1, 6.0, -.1, 8.6, '$F$', dx=-.75, dy=-.6)
    for (t, xt, yt, xb, yb) in [('lýtkový\nsval', -.9, 9.7, .9, 8.8), ('Achillova\nšlacha', -.9, 3.3, 1.75, 3.0), ('pata', -.9, .6, 1.6, .8)]:
        ax.text(xt, yt, t, fontsize=14, ha='right', va='center')
        ax.plot([xt + .1, xb], [yt, yb], color=INK, lw=.8)

if __name__ == '__main__':
    fig, ax = start(6, 4, osy=True)
    xs, ys = [0, 2, 3.2, 5.5, 7.5, 10], [0, .4, 1.4, 3.6, 4.6, 5]
    x = np.linspace(0, 10, 300); ax.plot(x, Pchip(xs, ys)(x), color=SILA)
    for (xi, t) in [(2.3, 'A'), (4.0, 'B'), (5.9, 'C'), (10, 'D')]:
        yi = Pchip(xs, ys)(xi); ax.plot(xi, yi, 'o', color=INK, ms=7); ax.text(xi - .4, yi + .25, t, fontsize=20)
    ax.set_xlim(0, 10.6); ax.set_ylim(0, 6.3)
    kval(ax, 'prodloužení šlachy', 'síla ve šlaše')
    ins = ax.inset_axes([0.6, 0.03, 0.4, 0.55]); motiv(ins)
    uloz(fig, '001_pruznost_modul_slachy.png')
