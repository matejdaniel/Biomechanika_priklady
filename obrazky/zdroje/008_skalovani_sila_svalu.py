from styl import *
from matplotlib.patches import Ellipse

def sval(ax, x0, y, L, d):
    """Sval jako vřeteno délky L a tloušťky d, se šlachami na obou koncích."""
    s = 0.18 * L
    ax.plot([x0, x0 + s], [y, y], color=INK, lw=2.4)
    ax.plot([x0 + L - s, x0 + L], [y, y], color=INK, lw=2.4)
    ax.add_patch(Ellipse((x0 + L / 2, y), L - 2 * s, d, fc=SVAL, ec=INK, lw=2))

fig, ax = start(6.4, 3.6)
sval(ax, 0.0, 1.0, 0.8, 0.22)
sval(ax, 1.5, 1.0, 2.4, 0.66)
kota(ax, 0.0, 0.55, 0.8, 0.55, '')
ax.text(0.4, 0.36, 'L', color=ROZMER, fontsize=26, ha='center', va='center', fontfamily='DejaVu Sans', fontstyle='italic')
kota(ax, 1.5, 0.45, 3.9, 0.45, '')
ax.text(2.7, 0.26, '3L', color=ROZMER, fontsize=26, ha='center', va='center', fontfamily='DejaVu Sans', fontstyle='italic')
sila(ax, 0.8, 1.0, 1.15, 1.0, '$F$', dx=-.12, dy=.1)
sila(ax, 3.9, 1.0, 4.35, 1.0, '$F\\,=\\,?$', dx=-.3, dy=.12)
ax.set_xlim(-.2, 4.6); ax.set_ylim(.0, 1.6)
uloz(fig, '008_skalovani_sila_svalu.png')
