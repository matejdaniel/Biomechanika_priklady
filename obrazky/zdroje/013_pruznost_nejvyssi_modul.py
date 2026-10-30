"""013 – Materiál s nejvyšším modulem: tahové křivky a)–c) + ilustrace endoprotézy kyčle
(013_pruznost_nejvyssi_modul_ilustrace.png) – materiály kov, plast, kost."""
from styl import *
import numpy as np
from PIL import Image
from scipy.interpolate import PchipInterpolator as Pchip
from pp_grafy1 import kval

ILU = '013_pruznost_nejvyssi_modul_ilustrace.png'

if __name__ == '__main__':
    fig = plt.figure(figsize=(6.4, 4), dpi=DPI); plt.close(fig)
    fig, ax = start(6.4, 4, osy=True)
    fig.subplots_adjust(left=.09, right=.6, bottom=.16, top=.95)
    C = {'a)': ('#4b3aa8', [0, .3, .45, .65, 1.0], [0, 2.4, 3.1, 3.5, 3.55]),
         'b)': ('#f77f00', [0, .06, .12, .4, .7], [0, 1.6, 2.2, 2.5, 2.6]),
         'c)': (INK, [0, .15, .28, .5, 1.0], [0, .9, 1.55, 1.65, 1.7])}
    for k, (c, xs, ys) in C.items():
        x = np.linspace(0, xs[-1], 200); ax.plot(x, Pchip(xs, ys)(x), color=c, lw=3)
        ax.text(xs[-1] + .03, ys[-1], k, color=c, fontsize=22, va='center')
    ax.set_xlim(0, 1.15); ax.set_ylim(0, 4.2)
    kval(ax, 'ε [–]', 'σ [MPa]')
    im = Image.open(ILU).convert('RGB'); a = np.asarray(im)
    ys, xs = np.where(a.min(2) < 225)
    k = np.asarray(im.crop((xs.min() - 10, ys.min() - 10, xs.max() + 10, ys.max() + 10))).copy(); k[k.min(2) > 235] = 255
    ax2 = fig.add_axes([.62, .08, .37, .78]); ax2.imshow(k); ax2.axis('off')
    ax2.text(k.shape[1] / 2, -60, 'endoprotéza kyčle:\nkov, plast a kost', fontsize=14, ha='center', va='bottom', linespacing=1.0)
    fig.savefig('013_pruznost_nejvyssi_modul.png', facecolor='white', dpi=DPI)
