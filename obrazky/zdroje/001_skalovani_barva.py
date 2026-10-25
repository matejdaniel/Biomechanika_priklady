from styl import *
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.patches import PathPatch
from matplotlib.transforms import Affine2D

def pismeno(ax, x, vyska):
    """Písmeno A (tiskové písmo) přesně dané výšky, levý dolní roh v (x, 0)."""
    p = TextPath((0, 0), 'A', size=1, prop=FontProperties(family='DejaVu Sans', weight='bold'))
    e = p.get_extents(); k = vyska / e.y1
    p = p.transformed(Affine2D().translate(-e.x0, 0).scale(k).translate(x, 0))
    ax.add_patch(PathPatch(p, color=INK, lw=0))

fig, ax = start(6, 4)
h1, h2 = 1.4, 0.7          # velikost písma 20 pt : 10 pt = 2 : 1
pismeno(ax, 0.0, h1)
pismeno(ax, 2.2, h2)
ax.plot([-.6, 3.6], [0, 0], color=INK, lw=1.2, alpha=.4)
kota(ax, -.25, 0, -.25, h1, '', dy=0)
ax.text(-.42, h1/2, '20 pt', color=ROZMER, fontsize=20, rotation=90, ha='center', va='center')
kota(ax, 3.1, 0, 3.1, h2, '', dy=0)
ax.text(3.27, h2/2, '10 pt', color=ROZMER, fontsize=20, rotation=90, ha='center', va='center')
ax.set_xlim(-.7, 3.6); ax.set_ylim(-.3, 1.7)
uloz(fig, '001_skalovani_barva.png')
