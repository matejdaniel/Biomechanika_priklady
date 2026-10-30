"""018 – Youngův modul s deformací v procentech: tahový diagram oceli + ilustrace nitrodřeňového hřebu
(018_pruznost_modul_procenta_ilustrace.png)."""
from styl import *
import numpy as np
from PIL import Image
from pp_grafy2 import mrizka, cz, krivka

ILU = '018_pruznost_modul_procenta_ilustrace.png'

if __name__ == '__main__':
    fig, ax = start(6, 4, osy=True)
    ax.plot([0, .8], [0, 1.5], color=SILA); krivka(ax, [.8, 1.0, 1.2], [1.5, 1.68, 1.8], color=SILA)
    for (x, y, t, dx, dy) in [(0, 0, 'A', .02, .08), (.8, 1.5, 'B', -.06, .1), (1.2, 1.8, 'C', .02, .03)]:
        ax.plot(x, y, 'o', color=INK, ms=6, clip_on=False); ax.text(x + dx, y + dy, t, fontsize=20)
    ax.set_xlim(0, 1.25); ax.set_ylim(0, 2.05)
    mrizka(ax, np.arange(0, 1.21, .2), np.arange(0, 2.01, .5), np.arange(0, 1.21, .05), np.arange(0, 2.01, .1))
    ax.set_xticklabels(cz(np.arange(0, 1.21, .2), 1)); ax.set_yticklabels(cz(np.arange(0, 2.01, .5), 1))
    ax.set_xlabel('ε [%]'); ax.set_ylabel('σ [GPa]')
    im = Image.open(ILU).convert('RGB'); a = np.asarray(im)
    ys, xs = np.where(a.min(2) < 225)
    k = np.asarray(im.crop((xs.min() - 10, ys.min() - 10, xs.max() + 10, ys.max() + 10))).copy(); k[k.min(2) > 235] = 255
    k = np.rot90(k, -1)                               # femur svisle (hlavice nahoře)
    fig.subplots_adjust(left=.17, right=.7, bottom=.25, top=.95)
    ax2 = fig.add_axes([.74, .04, .25, .92]); ax2.imshow(k); ax2.axis('off')
    ax2.set_xlim(-k.shape[1] * 1.0, k.shape[1] * 1.05)
    ax2.annotate('ocelový\nnitrodřeňový\nhřeb', xy=(k.shape[1] * .5, k.shape[0] * .62), xytext=(-k.shape[1] * .95, k.shape[0] * .5),
                 fontsize=13, ha='left', va='center', linespacing=1.0, arrowprops=dict(arrowstyle='-', color=INK, lw=1))
    fig.savefig('018_pruznost_modul_procenta.png', facecolor='white', dpi=DPI)
