"""Pružnost a pevnost – grafy (dávka 2)."""
from styl import *
import numpy as np
from scipy.interpolate import PchipInterpolator as Pchip
from pp_grafy1 import kval

def mrizka(ax, xmaj, ymaj, xmin=None, ymin=None):
    ax.set_xticks(xmaj); ax.set_yticks(ymaj)
    if xmin is not None: ax.set_xticks(xmin, minor=True)
    if ymin is not None: ax.set_yticks(ymin, minor=True)
    ax.grid(True, which='major', alpha=.35, lw=.9, color='#999999')
    ax.grid(True, which='minor', alpha=.2, lw=.6, color='#999999')
    for s in ('top', 'right'): ax.spines[s].set_visible(False)

def cz(vals, d=None):
    return [(f'{v:.{d}f}' if d is not None else f'{v:g}').replace('.', ',') for v in vals]

def krivka(ax, xs, ys, **kw):
    x = np.linspace(xs[0], xs[-1], 300); ax.plot(x, Pchip(xs, ys)(x), **kw)

def modul_procenta():
    fig, ax = start(6, 4, osy=True)
    ax.plot([0, .8], [0, 1.5], color=SILA); krivka(ax, [.8, 1.0, 1.2], [1.5, 1.68, 1.8], color=SILA)
    for (x, y, t, dx, dy) in [(0, 0, 'A', .02, .08), (.8, 1.5, 'B', -.06, .1), (1.2, 1.8, 'C', .02, .03)]:
        ax.plot(x, y, 'o', color=INK, ms=6, clip_on=False); ax.text(x + dx, y + dy, t, fontsize=20)
    ax.set_xlim(0, 1.25); ax.set_ylim(0, 2.05)
    mrizka(ax, np.arange(0, 1.21, .2), np.arange(0, 2.01, .5), np.arange(0, 1.21, .05), np.arange(0, 2.01, .1))
    ax.set_xticklabels(cz(np.arange(0, 1.21, .2), 1)); ax.set_yticklabels(cz(np.arange(0, 2.01, .5), 1))
    ax.set_xlabel('ε [%]'); ax.set_ylabel('σ [GPa]')
    uloz(fig, '018_pruznost_modul_procenta.png')

def vlakna(ax, x, y, typ, w=.55):
    """Malá ikona kolagenních vláken: zvlněná / napnutá / částečně / zcela přetržená."""
    xs = np.linspace(x - w / 2, x + w / 2, 60)
    for k in range(3):
        yy = y + (k - 1) * .16
        if typ == 'vlny': ax.plot(xs, yy + .05 * np.sin(xs * 40), color=INK, lw=1.4)
        elif typ == 'rovne': ax.plot(xs, np.full_like(xs, yy), color=INK, lw=1.4)
        else:
            mezera = (typ == 'pretrzene') or k == 1
            if mezera:
                ax.plot([x - w / 2, x - .05], [yy, yy], color=INK, lw=1.4); ax.plot([x + .05, x + w / 2], [yy, yy], color=INK, lw=1.4)
            else: ax.plot([x - w / 2, x + w / 2], [yy, yy], color=INK, lw=1.4)

def hooke():
    fig, ax = start(6, 4, osy=True)
    krivka(ax, [0, 1, 1.9, 2.1], [0, .15, .45, .6], color=SILA)
    ax.plot([2.1, 3.6], [.6, 5.0], color=SILA)
    krivka(ax, [3.6, 3.9, 4.5, 6.6], [5.0, 5.45, 5.6, 5.6], color=SILA)
    krivka(ax, [6.6, 6.8, 7.4, 8.1], [5.6, 5.4, 4.3, 2.4], color=SILA)
    for xv in (2.1, 3.75, 6.6): ax.axvline(xv, color=ROZMER, lw=1.1, ls='--', alpha=.6)
    for (xc, t) in [(1.05, 'A'), (2.9, 'B'), (5.2, 'C'), (7.6, 'D')]:
        ax.text(xc, 3.2 if t in 'AB' else 4.7, t, fontsize=22, ha='center')
    for (xc, t) in [(1.05, 'vlny'), (2.9, 'rovne'), (5.2, 'castecne'), (7.6, 'pretrzene')]: vlakna(ax, xc, 6.55, t)
    ax.set_xlim(0, 8.6); ax.set_ylim(0, 7.2)
    kval(ax, 'poměrná deformace ε', 'napětí σ')
    uloz(fig, '021_pruznost_hooke.png')

def max_sila_slacha():
    fig, ax = start(6, 4, osy=True)
    krivka(ax, [0, .02, .04, .07, .105, .13, .16, .2], [0, 4, 28, 80, 125, 140, 147, 150], color=SILA, lw=3)
    ax.set_xlim(0, .21); ax.set_ylim(0, 170)
    mrizka(ax, np.arange(0, .201, .04), np.arange(0, 161, 20), np.arange(0, .201, .01), np.arange(0, 161, 10))
    ax.set_xticklabels(cz(np.arange(0, .201, .04), 2))
    ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [MPa]')
    uloz(fig, '022_pruznost_max_sila_slacha.png')

def nahrady():
    fig, ax = start(6, 4, osy=True)
    ax.plot([0, .05, .25, .27, .34, .4], [0, 400, 1200, 1210, 1210, 1100], color='#1d3fa0', lw=3)
    ax.set_xlim(0, .42); ax.set_ylim(0, 1350)
    mrizka(ax, [0, .1, .2, .3, .4], [0, 400, 800, 1200], np.arange(0, .41, .025), np.arange(0, 1301, 100))
    ax.set_xticklabels(cz([0, .1, .2, .3, .4], 2))
    ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [MPa]')
    uloz(fig, '023_pruznost_nahrady.png')

def prodlouzeni_achilova():
    fig, ax = start(6, 4, osy=True)
    krivka(ax, [0, .025, .05, .075, .09, .1], [0, .75, 3.75, 4.5, 4.35, 3.0], color=SILA)
    ax.set_xlim(0, .105); ax.set_ylim(0, 5)
    yt = np.arange(0, 4.51, .75)
    mrizka(ax, [0, .025, .05, .075, .1], yt)
    ax.set_xticklabels(cz([0, .025, .05, .075, .1], 3)); ax.set_yticklabels(cz(yt, 2))
    ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [MPa]')
    uloz(fig, '024_pruznost_prodlouzeni_achilova.png')

def modul_elasticka_cast():
    fig, ax = start(6, 4, osy=True)
    ax.plot([0, .0005], [0, 100], color=SILA, lw=3); krivka(ax, [.0005, .00058, .0007, .003], [100, 118, 125, 125], color=SILA, lw=3)
    ax.set_xlim(0, .00305); ax.set_ylim(0, 155)
    mrizka(ax, [0, .001, .002, .003], [0, 50, 100, 150], np.arange(0, .00301, .0005), np.arange(0, 151, 25))
    ax.set_xticklabels(cz([0, .001, .002, .003], 3))
    ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [MPa]')
    uloz(fig, '025_pruznost_modul_elasticka_cast.png')

def tuhost_luku():
    fig, ax = start(6, 4, osy=True)
    ax.plot([0, .2, .5, .6], [0, 350, 350, 100], color=SILA)
    ax.set_xlim(0, .72); ax.set_ylim(0, 410)
    mrizka(ax, np.arange(0, .71, .1), np.arange(0, 401, 50))
    ax.set_xticklabels(cz(np.arange(0, .71, .1), 1))
    ax.set_xlabel('natažení tětivy x [m]'); ax.set_ylabel('síla F [N]')
    uloz(fig, '026_pruznost_tuhost_luku.png')

def ctyri_krivky(jmeno):
    fig, ax = start(6, 4, osy=True)
    K = {'A': (SILA, [0, .005, .009, .0125, .025], [0, 80, 96, 104, 115]),
         'B': (BOD, [0, .015, .019, .025], [0, 140, 152, 160]),
         'C': (ROZMER, [0, .015, .019, .025], [0, 100, 112, 120]),
         'D': (INK, [0, .005, .01, .0175], [0, 50, 60, 63])}
    for k, (c, xs, ys) in K.items():
        krivka(ax, xs, ys, color=c)
        dy = {'A': -6, 'C': 6}.get(k, 0)
        ax.text(xs[-1] + .0005, ys[-1] + dy, k, color=c, fontsize=22, va='center')
    for (x, y) in [(.005, 80), (.005, 50), (.015, 140), (.015, 100)]:
        ax.plot(x, y, 'o', color=INK, ms=6)
        ax.plot([x, x], [0, y], color=INK, lw=1, ls=':'); ax.plot([0, x], [y, y], color=INK, lw=1, ls=':')
    ax.set_xlim(0, .029); ax.set_ylim(0, 175)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.set_xticks([.005, .015]); ax.set_xticklabels(['0,005', '0,015']); ax.set_yticks([50, 80, 100, 140])
    ax.set_xlabel('ε [–]'); ax.set_ylabel('σ [MPa]')
    uloz(fig, jmeno)

def male_deformace():
    fig, ax = start(6, 4, osy=True)
    K = [('keramika', ROZMER, [0, .3], [0, 8.5], (.33, 8.3)),
         ('nerez. ocel 316', SILA, [0, 1.4, 1.8, 2.4, 3.2], [0, 5.5, 6.4, 6.8, 6.8], (3.3, 6.7)),
         ('běžný kov', BOD, [0, 2.8, 3.1, 3.5, 4.2, 5.3], [0, 5.0, 4.8, 5.4, 5.5, 5.2], (5.4, 5.1)),
         ('kost', '#e0a000', [0, 1.5, 3, 4.5, 6.2], [0, 2.4, 3.6, 3.9, 3.95], (6.3, 3.95)),
         ('UHMWPE', '#1d3fa0', [0, .7, 3, 6.2], [0, .8, 1.0, 1.25], (6.3, 1.25))]
    for (t, c, xs, ys, p) in K:
        krivka(ax, xs, ys, color=c); ax.text(*p, t, color=c, fontsize=18, va='center')
    krivka(ax, [0, 1.5, 2.3, 3.3, 4.3, 4.6], [0, .2, .8, 3.0, 4.95, 5.05], color=INK)
    ax.plot([4.6, 4.65], [5.05, 2.9], color=INK); ax.text(3.9, 2.4, 'vaz', fontsize=18)
    ax.set_xlim(0, 8.3); ax.set_ylim(0, 9.2)
    kval(ax, 'poměrná deformace ε', 'napětí σ')
    uloz(fig, '031_pruznost_male_deformace.png')

def mez_pevnosti():
    fig, ax = start(6, 4, osy=True)
    ax.plot([0, 2, 2.25], [0, 77, 385], color=SILA)
    for y in (77, 385): ax.plot([0, 2.25 if y == 385 else 2], [y, y], color=INK, lw=1, ls=':')
    ax.plot([2.25, 2.25], [0, 385], color=INK, lw=1, ls=':'); ax.plot([2, 2], [0, 77], color=INK, lw=1, ls=':')
    ax.set_xlim(0, 2.6); ax.set_ylim(0, 430)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.set_xticks([0, 1, 2, 2.25]); ax.set_xticklabels(['0', '1', '2', '2,25']); ax.set_yticks([0, 77, 385])
    ax.set_xlabel('ε [mm/mm]'); ax.set_ylabel('σ [MPa]')
    uloz(fig, '032_pruznost_mez_pevnosti.png')

def pet_materialu():
    fig, ax = start(6, 4, osy=True)
    K = {'A': ('#e0a000', [0, .4, .8], [0, 4, 8.3], (.75, 8.6)), 'B': ('#1aa3c8', [0, .8, 1.6, 2.2, 3], [0, 3.2, 6.5, 7.8, 7.2], (2.4, 8.1)),
         'C': (SILA, [0, 2, 4, 5.3], [0, 3.5, 7.2, 9.8], (4.8, 10.0)), 'D': (BOD, [0, 2, 4, 6.6], [0, 3.6, 6.2, 7.9], (6.3, 8.3)),
         'E': ('#1d3fa0', [0, 2, 3.5, 5, 8, 10, 13], [0, 3.2, 5.4, 6.2, 6.5, 7.3, 8.3], (11.8, 8.7)),
         'F': ('#e08a2a', [0, .4, 1.5, 6, 12.5], [0, 2.2, 3.0, 3.3, 3.9], (12.3, 4.25))}
    for k, (c, xs, ys, p) in K.items():
        krivka(ax, xs, ys, color=c); ax.text(*p, k, color=c, fontsize=20)
    ax.set_xlim(0, 15); ax.set_ylim(0, 10.8)
    mrizka(ax, [0, 5, 10, 15], [0, 2.5, 5, 7.5, 10])
    ax.set_yticklabels(cz([0, 2.5, 5, 7.5, 10], 1))
    ax.set_xlabel('poměrná deformace [%]'); ax.set_ylabel('napětí [MPa]')
    uloz(fig, '033_pruznost_pet_materialu.png')

def prumerny_modul():
    fig, ax = start(6, 4, osy=True)
    ax.plot([0, .02], [0, 1.0], color='#888888', lw=3); ax.text(.025, 1.0, 'A', fontsize=22)
    krivka(ax, [0, .08, .15, .2], [0, .2, .5, .95], color=ROZMER, lw=3); ax.text(.215, .93, 'B', fontsize=22)
    krivka(ax, [0, .2, .45, .7, 1.0], [0, .05, .3, .62, .75], color=INK, lw=3); ax.text(.985, .8, 'C', fontsize=22)
    ax.plot([0, 1.0], [.75, .75], color=INK, lw=2, ls='--')
    for x in (.2, 1.0): ax.plot([x, x], [0, .75 if x == 1 else .95], color=INK, lw=1.6)
    ax.set_xlim(0, 1.1); ax.set_ylim(0, 1.12)
    kval(ax, 'poměrná deformace ε', 'napětí σ')
    uloz(fig, '036_pruznost_prumerny_modul.png')

def kortikalni_kost():
    fig, ax = start(6, 4, osy=True)
    ax.axvspan(0, .7, color='#b48ac8', alpha=.15); ax.text(.35, 212, 'elastická\noblast', ha='center', va='top', fontsize=15, color='#7a4a90')
    krivka(ax, [0, .5, .95, 1.0, 1.2, 1.3, 1.7, 2.0], [0, 105, 205, 198, 120, 92, 88, 67], color=ROZMER)
    ax.text(1.05, 195, 'tlak', color=ROZMER, fontsize=20)
    krivka(ax, [0, .55, .7, 2.8], [0, 105, 115, 130], color=SILA, ls='--')
    ax.text(2.0, 135, 'tah', color=SILA, fontsize=20)
    ax.set_xlim(0, 3.0); ax.set_ylim(0, 235)
    mrizka(ax, np.arange(0, 3.01, .5), np.arange(0, 201, 50), None, np.arange(0, 221, 10))
    ax.set_xticklabels(cz(np.arange(0, 3.01, .5), 1))
    ax.set_xlabel('ε [%]'); ax.set_ylabel('σ [MPa]')
    uloz(fig, '040_pruznost_kortikalni_kost.png')

def sila_rychlost():
    fig, ax = start(6, 4, osy=True)
    krivka(ax, [0, .3, .8, 1.3], [4.5, 3.0, 1.1, 0], color=SILA); ax.text(.33, 3.3, 'A', fontsize=22, color=SILA)
    krivka(ax, [0, .4, 1.2, 2.0], [3.5, 2.0, .7, 0], color=ROZMER); ax.text(1.5, .7, 'B', fontsize=22, color=ROZMER)
    krivka(ax, [0, .3, .7, 1.0], [2.0, 1.0, .3, 0], color=BOD); ax.text(.32, .55, 'C', fontsize=22, color=BOD)
    ax.set_xlim(0, 2.2); ax.set_ylim(0, 5)
    kval(ax, 'rychlost kontrakce', 'síla')
    uloz(fig, '043_pruznost_sila_rychlost.png')

if __name__ == '__main__':
    modul_procenta(); hooke(); max_sila_slacha(); nahrady(); prodlouzeni_achilova(); modul_elasticka_cast(); tuhost_luku()
    ctyri_krivky('029_pruznost_nejmensi_modul.png'); ctyri_krivky('035_pruznost_material_a.png')
    male_deformace(); mez_pevnosti(); pet_materialu(); prumerny_modul(); kortikalni_kost(); sila_rychlost()
