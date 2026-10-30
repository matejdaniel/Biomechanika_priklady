"""014 – Youngův modul v elastické oblasti: tahová křivka vazu + ilustrace kolene s předním zkříženým vazem
(014_pruznost_modul_elasticka_ilustrace.png)."""
from styl import *
import numpy as np
from PIL import Image
from scipy.interpolate import PchipInterpolator as Pchip

ILU = '014_pruznost_modul_elasticka_ilustrace.png'

if __name__ == '__main__':
    fig, ax = start(6.4, 4, osy=True)
    fig.subplots_adjust(left=.15, right=.62, bottom=.22, top=.95)
    x = np.linspace(0, .19, 400)
    ax.plot(x, Pchip([0, .015, .025, .03, .06, .07, .1, .14, .19], [0, 1, 8, 20, 115, 125, 138, 142, 144])(x), color=SILA, lw=3)
    ax.set_xlim(0, .2); ax.set_ylim(0, 155)
    ax.set_xticks([0, .05, .1, .15, .2]); ax.set_xticklabels(['0', '0,05', '0,1', '0,15', '0,2'])
    ax.set_yticks([0, 50, 100, 150])
    ax.set_xticks(np.arange(0, .201, .01), minor=True); ax.set_yticks(np.arange(0, 151, 10), minor=True)
    ax.grid(True, which='major', alpha=.35, lw=.9, color='#999999'); ax.grid(True, which='minor', alpha=.2, lw=.6, color='#999999')
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [MPa]')
    im = Image.open(ILU).convert('RGB'); a = np.asarray(im)
    ys, xs = np.where(a.min(2) < 225); x0, y0 = xs.min() - 10, ys.min() - 10
    k = np.asarray(im.crop((x0, y0, xs.max() + 10, ys.max() + 10))).copy(); k[k.min(2) > 235] = 255
    ax2 = fig.add_axes([.63, .05, .36, .85]); ax2.imshow(k); ax2.axis('off')
    ax2.set_xlim(-420, k.shape[1] + 20)
    bx, by = 1040 - x0, 980 - y0
    ax2.annotate('přední\nzkřížený\nvaz', xy=(bx, by), xytext=(-410, by - 200), fontsize=14, ha='left', va='center',
                 linespacing=1.0, arrowprops=dict(arrowstyle='-', color=INK, lw=1))
    fig.savefig('014_pruznost_modul_elasticka.png', facecolor='white', dpi=DPI)
