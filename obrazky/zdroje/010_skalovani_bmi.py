from styl import *
from matplotlib.patches import Ellipse, FancyBboxPatch, Rectangle

fig, ax = start(6, 5)
cx, y0 = 0.9, .14
# váha
ax.add_patch(FancyBboxPatch((cx-.5, 0), 1.0, .12, boxstyle='round,pad=0.02', fc='#dddddd', ec=INK, lw=2))
ax.add_patch(Rectangle((cx-.2, .025), .4, .07, fc='white', ec=INK, lw=1.2))
ax.text(cx, .06, '? kg', fontsize=15, ha='center', va='center')
# schematický člověk (výška 1,8 jednotky = 180 cm)
for s in (-1, 1):
    ax.plot([cx+s*.08, cx+s*.09], [y0+.02, y0+.86], color=KUZE, lw=11, solid_capstyle='round', zorder=1)
    ax.plot([cx+s*.08, cx+s*.09], [y0+.02, y0+.86], color=INK, lw=13, solid_capstyle='round', zorder=0)
    ax.plot([cx+s*.2, cx+s*.27], [y0+1.38, y0+.88], color=KUZE, lw=8, solid_capstyle='round', zorder=1)
    ax.plot([cx+s*.2, cx+s*.27], [y0+1.38, y0+.88], color=INK, lw=10, solid_capstyle='round', zorder=0)
ax.add_patch(FancyBboxPatch((cx-.17, y0+.84), .34, .58, boxstyle='round,pad=0.04', fc=KUZE, ec=INK, lw=2, zorder=2))
ax.add_patch(Ellipse((cx, y0+1.63), .24, .3, fc=KUZE, ec=INK, lw=2, zorder=2))
H = y0 + 1.79
kota(ax, cx+.55, y0, cx+.55, H, '', dy=0)
ax.text(cx+.7, (y0+H)/2, '180 cm', color=ROZMER, fontsize=20, rotation=90, ha='center', va='center')
ax.text(-1.0, 1.25, 'V = 100 dm³', fontsize=22)
ax.text(-1.0, 1.0, 'ρ = 1020 kg/m³', fontsize=22)
ax.set_xlim(-1.1, 1.75); ax.set_ylim(-.12, 2.05)
uloz(fig, '010_skalovani_bmi.png')
