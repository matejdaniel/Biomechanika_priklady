"""020 – Tuhost pružiny: pružina se závažím (kóty) + ilustrace expandéru z Gemini (020_pruznost_tuhost_pruziny_ilustrace.png)."""
from styl import *
import numpy as np
from PIL import Image
from matplotlib.patches import Rectangle, FancyBboxPatch

ILU = '020_pruznost_tuhost_pruziny_ilustrace.png'

def pruzina(ax, x, y0, y1, n=10, w=.22):
    ys = np.linspace(y0, y1, 2 * n + 1)
    xs = [x + (w if i % 2 else -w) if 0 < i < 2 * n else x for i in range(2 * n + 1)]
    ax.plot(xs, ys, color='#6d7a86', lw=2.2)

if __name__ == '__main__':
    fig, ax = start(6.4, 4)
    fig.subplots_adjust(left=.0, right=.5, bottom=.02, top=.98)
    ax.add_patch(Rectangle((-.8, 3.0), 3.4, .15, fc='#bbbbbb', ec=INK, lw=2))
    for x in np.linspace(-.75, 2.4, 12): ax.plot([x, x + .15], [3.15, 3.33], color=INK, lw=1.1)
    pruzina(ax, 0, 3.0, 1.0)                                  # volná pružina
    pruzina(ax, 1.7, 3.0, .55)                                 # pružina se závažím
    ax.add_patch(FancyBboxPatch((1.4, -.1), .6, .6, boxstyle='round,pad=0.02', fc='#999999', ec=INK, lw=2))
    ax.text(1.7, .2, '2 kg', color='white', fontsize=17, ha='center', va='center')
    ax.plot([-.35, 2.15], [1.0, 1.0], color=ROZMER, lw=1, ls=':'); ax.plot([1.45, 2.15], [.55, .55], color=ROZMER, lw=1, ls=':')
    kota(ax, -.45, 1.0, -.45, 3.0, '', dy=0); ax.text(-.6, 2.0, '10 cm', color=ROZMER, fontsize=17, ha='right', va='center')
    kota(ax, 2.1, .55, 2.1, 1.0, '', dy=0); ax.text(2.25, .82, '4 mm', color=ROZMER, fontsize=16, va='center')
    ax.text(2.25, .62, '(zvětšeno)', color=ROZMER, fontsize=11, va='center')
    ax.text(.3, .1, '$k$ = ?', color=ROZMER, fontsize=22, ha='center', va='center')
    ax.set_xlim(-1.6, 3.1); ax.set_ylim(-.5, 3.5)
    im = Image.open(ILU).convert('RGB'); a = np.asarray(im)
    ys, xs = np.where(a.min(2) < 225)
    k = np.asarray(im.crop((xs.min() - 10, ys.min() - 10, xs.max() + 10, ys.max() + 10))).copy(); k[k.min(2) > 235] = 255
    ax2 = fig.add_axes([.52, .12, .46, .76]); ax2.imshow(k); ax2.axis('off')
    ax2.text(k.shape[1] / 2, k.shape[0] + 60, 'pružinový expandér', fontsize=15, ha='center', va='top')
    fig.savefig('020_pruznost_tuhost_pruziny.png', facecolor='white', dpi=DPI)
