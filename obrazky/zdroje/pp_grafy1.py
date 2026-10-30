"""Pružnost a pevnost – grafy (dávka 1). Každý obrázek je samostatná funkce."""
from styl import *
import numpy as np
from scipy.interpolate import PchipInterpolator as Pchip

def kval(ax, xl, yl):
    """Kvalitativní graf: osy se šipkami, bez hodnot."""
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel(xl); ax.set_ylabel(yl)
    ax.plot(1, 0, '>', color=INK, transform=ax.get_yaxis_transform(), clip_on=False, ms=9)
    ax.plot(0, 1, '^', color=INK, transform=ax.get_xaxis_transform(), clip_on=False, ms=9)

def slacha(jmeno, body=True, useky=True):
    fig, ax = start(6, 4, osy=True)
    x = np.linspace(0, 10, 300)
    f = Pchip([0, 2, 3.2, 5.5, 7.5, 10], [0, .4, 1.4, 3.6, 4.6, 5])(x)
    ax.plot(x, f, color=SILA)
    if body:
        for (xi, t) in [(2.3, 'A'), (4.0, 'B'), (5.9, 'C'), (10, 'D')]:
            yi = Pchip([0, 2, 3.2, 5.5, 7.5, 10], [0, .4, 1.4, 3.6, 4.6, 5])(xi)
            ax.plot(xi, yi, 'o', color=INK, ms=7); ax.text(xi - .35, yi + .25, t, fontsize=20)
    if useky:
        for xi in (2.6, 6.4):
            ax.axvline(xi, color=ROZMER, lw=1.2, ls='--', alpha=.6)
        for (xc, t) in [(1.3, 'I'), (4.5, 'II'), (8.2, 'III')]:
            ax.text(xc, 5.7, t, color=ROZMER, fontsize=22, ha='center', fontfamily='DejaVu Serif')
    ax.set_xlim(0, 10.6); ax.set_ylim(0, 6.3)
    kval(ax, 'prodloužení', 'síla')
    uloz(fig, jmeno)

def slitina():
    fig, ax = start(6, 4, osy=True)
    x = np.linspace(0, 0.035, 300)
    y = Pchip([0, .01, .013, .02, .028, .035], [0, 2.0, 2.35, 2.65, 2.8, 2.85])(x)
    ax.plot(x, y, color=SILA)
    ax.set_xlim(0, .036); ax.set_ylim(0, 3.6)
    ax.set_xticks([0, .01, .02, .03]); ax.set_xticklabels(['0', '0,01', '0,02', '0,03'])
    ax.set_yticks([0, 1, 2, 3])
    ax.set_xticks(np.arange(0, .036, .0025), minor=True); ax.set_yticks(np.arange(0, 3.6, .25), minor=True)
    ax.grid(True, which='major', alpha=.35, lw=.9, color='#999999'); ax.grid(True, which='minor', alpha=.2, lw=.6, color='#999999')
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [kPa]')
    uloz(fig, '005_pruznost_slitina.png')

def biceps_kone():
    fig, ax = start(6, 4, osy=True)
    x1 = np.linspace(0, 18.8, 200); y1 = Pchip([0, 5, 10, 15, 17.5, 18.8], [0, 2, 4, 6.3, 8.6, 11.5])(x1)
    x2 = np.linspace(0, 17.5, 200); y2 = Pchip([0, 5, 10, 15, 17.5], [0, 2, 4, 6, 7.0])(x2)
    ax.plot(x1, y1, color=SILA, label='in vivo'); ax.plot(x2, y2, color=ROZMER, label='in vitro')
    ax.plot([17.5, 17.2], [7.0, 6.2], color=ROZMER)       # přetržení vzorku
    ax.text(9.5, 5.6, 'in vivo', color=SILA, fontsize=20); ax.text(13.6, 3.9, 'in vitro', color=ROZMER, fontsize=20)
    ax.set_xlim(0, 21); ax.set_ylim(0, 12.5)
    ax.set_xticks(range(0, 21, 5)); ax.set_yticks(range(0, 13, 2))
    graf(ax); ax.set_xlabel('prodloužení [mm]'); ax.set_ylabel('síla [kN]')
    uloz(fig, '006_pruznost_biceps_kone.png')

def rychlost_zatezovani():
    fig, ax = start(6, 4, osy=True)
    C = {'A': (SILA, [0, .1, .2, .35], [0, 5.2, 6.6, 7.0]), 'B': (ROZMER, [0, .3, .5, .7], [0, 3.6, 5.6, 5.9]),
         'C': ('#f77f00', [0, .5, 1.0, 1.35], [0, 1.6, 2.9, 3.1]), 'D': (BOD, [0, .5, 1.0, 1.35], [0, 1.1, 1.9, 2.0])}
    for k, (c, xs, ys) in C.items():
        x = np.linspace(0, xs[-1], 200); ax.plot(x, Pchip(xs, ys)(x), color=c)
        ax.text(xs[-1] + .04, ys[-1], k, color=c, fontsize=22, va='center')
    ax.set_xlim(0, 1.6); ax.set_ylim(0, 7.8)
    kval(ax, 'poměrné prodloužení ε', 'napětí σ')
    uloz(fig, '007_pruznost_rychlost_zatezovani.png')

def body_diagramu():
    fig, ax = start(6, 4, osy=True)
    x = np.linspace(.05, 1, 300)
    y = np.r_[Pchip([.05, .14, .3, .55, .7, 1], [3.6, 3.45, 3.85, 4.75, 4.85, 4.1])(x)]
    ax.plot([0, .05], [0, 3.6], color=SILA); ax.plot(x, y, color=SILA)
    for (xi, t) in [(.14, 'A'), (.62, 'B')]:
        yi = Pchip([.05, .14, .3, .55, .7, 1], [3.6, 3.45, 3.85, 4.75, 4.85, 4.1])(xi)
        ax.plot(xi, yi, 'x', color=INK, ms=11, mew=2); ax.text(xi - .02, yi + .35, t, fontsize=22)
    ax.set_xlim(0, 1.08); ax.set_ylim(0, 5.8)
    kval(ax, 'poměrná deformace ε', 'napětí σ')
    uloz(fig, '012_pruznost_body_diagramu.png')

def nejvyssi_modul():
    fig, ax = start(6, 4, osy=True)
    C = {'a)': ('#4b3aa8', [0, .3, .45, .65, 1.0], [0, 2.4, 3.1, 3.5, 3.55]),
         'b)': ('#f77f00', [0, .06, .12, .4, .7], [0, 1.6, 2.2, 2.5, 2.6]),
         'c)': (INK, [0, .15, .28, .5, 1.0], [0, .9, 1.55, 1.65, 1.7])}
    for k, (c, xs, ys) in C.items():
        x = np.linspace(0, xs[-1], 200); ax.plot(x, Pchip(xs, ys)(x), color=c, lw=3)
        ax.text(xs[-1] + .03, ys[-1], k, color=c, fontsize=22, va='center')
    ax.set_xlim(0, 1.15); ax.set_ylim(0, 4.2)
    kval(ax, 'ε [–]', 'σ [MPa]')
    uloz(fig, '013_pruznost_nejvyssi_modul.png')

def modul_elasticka():
    fig, ax = start(6, 4, osy=True)
    x = np.linspace(0, .19, 400)
    y = Pchip([0, .015, .025, .03, .06, .07, .1, .14, .19], [0, 1, 8, 20, 115, 125, 138, 142, 144])(x)
    ax.plot(x, y, color=SILA, lw=3)
    ax.set_xlim(0, .2); ax.set_ylim(0, 155)
    ax.set_xticks([0, .05, .1, .15, .2]); ax.set_xticklabels(['0', '0,05', '0,1', '0,15', '0,2'])
    ax.set_yticks([0, 50, 100, 150])
    ax.set_xticks(np.arange(0, .201, .01), minor=True); ax.set_yticks(np.arange(0, 151, 10), minor=True)
    ax.grid(True, which='major', alpha=.35, lw=.9, color='#999999'); ax.grid(True, which='minor', alpha=.2, lw=.6, color='#999999')
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [MPa]')
    uloz(fig, '014_pruznost_modul_elasticka.png')

def modul_diagram():
    fig, ax = start(6, 4, osy=True)
    x = np.r_[np.linspace(0, .0028, 20), np.linspace(.0028, .26, 300)]
    y = np.r_[np.linspace(0, 44, 20), Pchip([.0028, .01, .04, .08, .14, .2, .26], [44, 50, 61, 70, 75, 70, 55])(np.linspace(.0028, .26, 300))]
    ax.plot(x, y, color=SILA)
    for (xi, yi, t, dx, dy) in [(0, 0, 'E (0; 0)', .006, 2), (.0028, 44, 'F (0,0028; 44)', .008, -6), (.26, 55, 'G (0,26; 55)', -.03, 5)]:
        ax.plot(xi, yi, 'o', color=INK, ms=7, clip_on=False); ax.text(xi + dx, yi + dy, t, fontsize=17)
    ax.set_xlim(0, .3); ax.set_ylim(0, 85)
    ax.set_xticks(np.arange(0, .29, .04)); ax.set_xticklabels(['0', '0,04', '0,08', '0,12', '0,16', '0,20', '0,24', '0,28'])
    ax.set_yticks(range(0, 81, 10))
    graf(ax); ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [MPa]')
    uloz(fig, '016_pruznost_modul_diagram.png')

if __name__ == '__main__':
    slacha('001_pruznost_modul_slachy.png', body=True, useky=False)
    slacha('002_pruznost_poruseni_vlaken.png', body=False, useky=True)
    slitina(); biceps_kone(); rychlost_zatezovani(); body_diagramu(); nejvyssi_modul(); modul_elasticka(); modul_diagram()
