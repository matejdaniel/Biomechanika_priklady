"""016 – Youngův modul z tahového diagramu (plast UHMWPE) + ilustrace endoprotézy kolene
(016_pruznost_modul_diagram_ilustrace.png)."""
from styl import *
import numpy as np
from PIL import Image
from scipy.interpolate import PchipInterpolator as Pchip

ILU = '016_pruznost_modul_diagram_ilustrace.png'

if __name__ == '__main__':
    fig, ax = start(6.4, 4, osy=True)
    fig.subplots_adjust(left=.13, right=.62, bottom=.22, top=.95)
    xx = np.linspace(.0028, .26, 300)
    x = np.r_[np.linspace(0, .0028, 20), xx]
    y = np.r_[np.linspace(0, 44, 20), Pchip([.0028, .01, .04, .08, .14, .2, .26], [44, 50, 61, 70, 75, 70, 55])(xx)]
    ax.plot(x, y, color=SILA)
    for (xi, yi, t, dx, dy) in [(0, 0, 'E (0; 0)', .008, 3), (.0028, 44, 'F (0,0028; 44)', .01, -7), (.26, 55, 'G (0,26; 55)', -.075, -9)]:
        ax.plot(xi, yi, 'o', color=INK, ms=7, clip_on=False); ax.text(xi + dx, yi + dy, t, fontsize=15)
    ax.set_xlim(0, .3); ax.set_ylim(0, 85)
    ax.set_xticks([0, .08, .16, .24]); ax.set_xticklabels(['0', '0,08', '0,16', '0,24']); ax.set_xticks(np.arange(0, .29, .04), minor=True)
    ax.set_yticks(range(0, 81, 10))
    graf(ax); ax.grid(True, which='minor', alpha=.3, lw=.8, color='#999999'); ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [MPa]')
    im = Image.open(ILU).convert('RGB'); a = np.asarray(im)
    ys, xs = np.where(a.min(2) < 225); x0, y0 = xs.min() - 10, ys.min() - 10
    k = np.asarray(im.crop((x0, y0, xs.max() + 10, ys.max() + 10))).copy(); k[k.min(2) > 235] = 255
    ax2 = fig.add_axes([.6, .04, .39, .9]); ax2.imshow(k); ax2.axis('off')
    ax2.set_xlim(-620, k.shape[1] + 10)
    bx, by = 760 - x0, 1100 - y0
    ax2.annotate('plastová\nvložka\n(polyetylen)', xy=(bx, by), xytext=(-600, by - 260), fontsize=14, ha='left', va='center',
                 linespacing=1.0, arrowprops=dict(arrowstyle='-', color=INK, lw=1))
    fig.savefig('016_pruznost_modul_diagram.png', facecolor='white', dpi=DPI)
