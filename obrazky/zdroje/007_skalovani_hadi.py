from styl import *
import numpy as np
from matplotlib.patches import Ellipse

def had(ax, x0, y0, delka, tl):
    """Zjednodušený had: vlnitá čára dané délky (v souřadnicích obrázku) s hlavou."""
    x = np.linspace(0, delka, 200); y = 0.12 * np.sin(x / delka * 4 * np.pi) * min(1, delka)
    ax.plot(x0 + x, y0 + y, color='#7a5c3a', lw=tl, solid_capstyle='round')
    ax.add_patch(Ellipse((x0 + delka + .04, y0 + y[-1]), .16 * tl / 9, .1 * tl / 9, color='#7a5c3a'))

fig, ax = start(6.4, 4.6)
# horní řada: celí hadi, délky v poměru 43 : 188
had(ax, 0.0, 2.35, 0.55, 5);  kota(ax, 0.0, 2.05, 0.6, 2.05, '43 cm', dy=-.17)
had(ax, 1.2, 2.35, 2.4, 11);  kota(ax, 1.2, 2.05, 3.66, 2.05, '188 cm', dy=-.17)
ax.text(0.3, 2.75, 'malý jedinec', ha='center', fontsize=18)
ax.text(2.4, 2.75, 'velký jedinec', ha='center', fontsize=18)
# dolní řada: průřezy ve skutečném poměru (1 cm = 0,25 jednotky)
s = 0.25
ax.add_patch(Ellipse((0.3, 0.75), .45*s*2, .8*s*2, fc='#d9c3a0', ec=INK, lw=2))
ax.add_patch(Ellipse((2.4, 0.7), 2*s*2, 3.5*s*2, fc='#d9c3a0', ec=INK, lw=2))
kota(ax, 0.3-.45*s, 0.22, 0.3+.45*s, 0.22, '0,45 cm', dy=-.17)
kota(ax, 0.62, 0.75-.8*s, 0.62, 0.75+.8*s, '', dy=0); ax.text(.72, .75, '0,8 cm', color=ROZMER, fontsize=18, va='center')
kota(ax, 2.4-2*s, -0.3, 2.4+2*s, -0.3, '2 cm', dy=-.17)
kota(ax, 3.05, 0.7-3.5*s, 3.05, 0.7+3.5*s, '', dy=0); ax.text(3.15, .7, '3,5 cm', color=ROZMER, fontsize=18, va='center')
ax.text(-.15, 1.5, 'průřez středem těla:', ha='left', fontsize=18, alpha=.8)
ax.set_xlim(-.2, 3.9); ax.set_ylim(-.55, 2.95)
uloz(fig, '007_skalovani_hadi.png')
