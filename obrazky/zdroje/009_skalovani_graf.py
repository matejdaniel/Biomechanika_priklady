"""009 – Graf mocninové závislosti: stejná závislost y = x² v lineárních (vlevo)
a v logaritmických souřadnicích (vpravo). Osy záměrně bez popisků a hodnot."""
from styl import *
import numpy as np

plt.xkcd(scale=0.8, length=120, randomness=2)
start()                                   # nastaví font a barvy stylu
plt.close('all')
fig, (a1, a2) = plt.subplots(1, 2, figsize=(W, H), dpi=DPI)
x = np.linspace(0.1, 10, 300)
a1.plot(x, x ** 2, color=SILA)
a2.loglog(x, x ** 2, color=SILA)
for ax in (a1, a2):
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([]); ax.minorticks_off()
    ax.set_xticklabels([]); ax.set_yticklabels([])
    ax.tick_params(which='both', length=0)
a1.set_xlim(0, 10.5); a1.set_ylim(0, 105)
a2.set_xlim(0.09, 12); a2.set_ylim(0.008, 150)
a1.set_title('A', fontsize=24); a2.set_title('B', fontsize=24)
fig.subplots_adjust(wspace=.45)
# šipka mezi grafy (přechod z A do B)
from matplotlib.patches import FancyArrowPatch
b1, b2 = a1.get_position(), a2.get_position()
y = (b1.y0 + b1.y1) / 2
fig.patches.append(FancyArrowPatch((b1.x1 + .02, y), (b2.x0 - .02, y), transform=fig.transFigure,
                                   arrowstyle='-|>', mutation_scale=26, lw=3.2, color='#888888'))
fig.savefig('009_skalovani_graf.png', facecolor='white', dpi=DPI)
