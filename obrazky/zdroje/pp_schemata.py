"""Pružnost a pevnost – schémata."""
from styl import *
import numpy as np
from matplotlib.patches import Rectangle, Ellipse, FancyBboxPatch, Polygon, Circle

KOSTB = '#e9d8b4'

def valec(ax, x0, x1, y, r, fc=KOSTB, dutina=None):
    """Válec (kost, šlacha, drát) ležící vodorovně, s eliptickými čely."""
    ax.add_patch(Rectangle((x0, y - r), x1 - x0, 2 * r, fc=fc, ec='none', zorder=1))
    ax.plot([x0, x1], [y + r, y + r], color=INK, lw=2.2, zorder=2); ax.plot([x0, x1], [y - r, y - r], color=INK, lw=2.2, zorder=2)
    ax.add_patch(Ellipse((x0, y), .35 * r, 2 * r, fc=fc, ec=INK, lw=2.2, zorder=3))
    if dutina: ax.add_patch(Ellipse((x0, y), .35 * dutina, 2 * dutina, fc='white', ec=INK, lw=1.6, zorder=4))
    ax.add_patch(Ellipse((x1, y), .35 * r, 2 * r, fc=fc, ec=INK, lw=2.2, zorder=3, theta1=-90, theta2=90) if False else
                 Ellipse((x1, y), .35 * r, 2 * r, fc=fc, ec=INK, lw=2.2, zorder=0))

def kost_tah():
    fig, ax = start(6, 3.2)
    valec(ax, 0, 3, 0, .45)
    sila(ax, 0, 0, -1.0, 0, '$F$', dx=-.05, dy=.12); sila(ax, 3, 0, 4.0, 0, '$F$ = 100 N', dx=-.55, dy=.12)
    kota(ax, 2.2, -.45, 2.2, .45, '', dy=0); ax.text(1.5, .7, '$d$ = 5 cm', color=ROZMER, fontsize=18, ha='center')
    ax.plot([1.75, 2.2], [.62, .45], color=ROZMER, lw=1)
    ax.text(1.5, -.8, '$E$ = 10 GPa', fontsize=20, ha='center')
    ax.set_xlim(-1.4, 4.4); ax.set_ylim(-1.05, 1.0)
    uloz(fig, '003_pruznost_deformace_kosti.png')

def drat():
    fig, ax = start(4.5, 5)
    ax.add_patch(Rectangle((-.9, 3.0), 1.8, .18, fc='#bbbbbb', ec=INK, lw=2))
    for x in np.linspace(-.85, .8, 10): ax.plot([x, x + .15], [3.18, 3.36], color=INK, lw=1.2)
    ax.plot([0, 0], [3.0, .6], color='#777777', lw=2.5)
    ax.add_patch(FancyBboxPatch((-.35, 0), .7, .6, boxstyle='round,pad=0.02', fc='#999999', ec=INK, lw=2))
    sila(ax, 0, .2, 0, -.6, '$F$ = 115 N', dx=.1, dy=.05)
    kota(ax, .55, .6, .55, 3.0, '', dy=0); ax.text(.68, 1.8, '$L$ = 1,12 m', color=ROZMER, fontsize=18, va='center')
    ax.text(-.12, 2.2, '$S$ = 6,0·10$^{-3}$ cm²', fontsize=17, ha='right')
    ax.text(-.12, 1.85, '$E$ = 20·10$^{10}$ N/m²', fontsize=17, ha='right')
    ax.set_xlim(-1.6, 1.8); ax.set_ylim(-.8, 3.5)
    uloz(fig, '004_pruznost_prodlouzeni_dratu.png')

def sval_pcsa():
    fig, ax = start(6, 3.4)
    e = Ellipse((1.5, 0), 2.6, .9, fc=SVAL, ec=INK, lw=2, zorder=2); ax.add_patch(e)
    t = np.linspace(-1, 1, 100)
    for f in np.linspace(-.7, .7, 5):
        ln, = ax.plot(1.5 + 1.3 * t, f * .45 * np.sqrt(1 - t ** 2), color='white', lw=1.4, alpha=.85, zorder=3); ln.set_clip_path(e)
    ax.plot([-.4, .2], [0, 0], color=INK, lw=2.4); ax.plot([2.8, 3.4], [0, 0], color=INK, lw=2.4)
    ax.plot([1.5, 1.5], [-.45, .45], color=ROZMER, lw=1.6, ls='--', zorder=4)
    ax.add_patch(Ellipse((4.3, 0), .5, .9, fc=SVAL, ec=INK, lw=2))
    ax.text(4.3, -.75, 'PCSA = 2750 mm²', color=ROZMER, fontsize=18, ha='center')
    ax.text(4.3, .62, 'příčný řez', fontsize=17, ha='center')
    sila(ax, 3.4, 0, 3.9, 0) if False else None
    ax.text(1.5, -.8, 'σ = 1 MPa', fontsize=20, ha='center')
    ax.set_xlim(-.6, 5.3); ax.set_ylim(-1.0, 1.0)
    uloz(fig, '008_pruznost_max_sila_svalu.png')

def vaz():
    fig, ax = start(6, 3.2)
    ax.add_patch(Rectangle((-.4, -.7), .4, 1.4, fc='#cccccc', ec=INK, lw=2))
    valec(ax, 0, 2.5, 0, .3, fc='#f3e7d3')
    ax.plot([2.5, 2.75], [0, 0], color=INK, lw=2)
    ax.plot([2.75, 2.75], [-.3, .3], color='#999999', lw=2, ls='--')
    sila(ax, 2.75, 0, 3.6, 0, '$F$ = 100 N', dx=-.6, dy=.15)
    kota(ax, 0, -.55, 2.5, -.55, '5 cm', dy=-.18)
    kota(ax, 2.5, .5, 2.75, .5, '', dy=0); ax.text(2.62, .7, '1 mm', color=ROZMER, fontsize=17, ha='center')
    ax.text(1.25, .55, '$S$ = 1 cm²', fontsize=18, ha='center')
    ax.set_xlim(-.6, 3.9); ax.set_ylim(-1.0, 1.0)
    uloz(fig, '015_pruznost_modul_vazu.png')

def pruzina_draw(ax, x, y0, y1, n=9, w=.18):
    ys = np.linspace(y0, y1, 2 * n + 1); xs = [x + (w if i % 2 else -w) if 0 < i < 2 * n else x for i in range(2 * n + 1)]
    ax.plot(xs, ys, color=INK, lw=2)

def pruzina():
    fig, ax = start(5, 4.5)
    ax.add_patch(Rectangle((-.7, 3.0), 3.0, .15, fc='#bbbbbb', ec=INK, lw=2))
    pruzina_draw(ax, 0, 3.0, 1.0)
    pruzina_draw(ax, 1.6, 3.0, .8)
    ax.add_patch(FancyBboxPatch((1.3, .2), .6, .55, boxstyle='round,pad=0.02', fc='#999999', ec=INK, lw=2))
    ax.text(1.6, .47, '2 kg', color='white', fontsize=18, ha='center', va='center')
    ax.plot([-.3, 2.1], [1.0, 1.0], color=ROZMER, lw=1, ls=':'); ax.plot([1.3, 2.1], [.8, .8], color=ROZMER, lw=1, ls=':')
    kota(ax, -.45, 1.0, -.45, 3.0, '', dy=0); ax.text(-.58, 2.0, '10 cm', color=ROZMER, fontsize=18, ha='right', va='center')
    kota(ax, 2.05, .8, 2.05, 1.0, '', dy=0); ax.text(2.18, .9, '4 mm', color=ROZMER, fontsize=18, va='center')
    ax.set_xlim(-1.4, 2.9); ax.set_ylim(0, 3.4)
    uloz(fig, '020_pruznost_tuhost_pruziny.png')

def trubice(jmeno, R, r, txt_R, txt_r, F, extra=None, delka=None, polomer=False):
    fig, ax = start(6, 4)
    # boční řez dutou kostí pod tuhou deskou
    h = 2.4
    for x0 in (-R, r):
        ax.add_patch(Rectangle((x0, 0), R - r, h, fc=KOSTB, ec=INK, lw=2, hatch='///' if False else None))
    ax.add_patch(Rectangle((-r, 0), 2 * r, h, fc='#f7f0e2', ec='none'))
    ax.add_patch(Rectangle((-R - .15, h), 2 * R + .3, .15, fc='#888888', ec=INK, lw=2))
    ax.add_patch(Rectangle((-R - .15, -.15), 2 * R + .3, .15, fc='#bbbbbb', ec=INK, lw=2))
    sila(ax, 0, h + .9, 0, h + .17, F, dx=.12, dy=.3)
    if delka: kota(ax, R + .35, 0, R + .35, h, '', dy=0); ax.text(R + .5, h / 2, delka, color=ROZMER, fontsize=20, va='center')
    # průřez
    cx = 3.0; cy = 1.2
    ax.add_patch(Circle((cx, cy), R, fc=KOSTB, ec=INK, lw=2)); ax.add_patch(Circle((cx, cy), r, fc='white', ec=INK, lw=1.8))
    if polomer:
        from matplotlib.patches import FancyArrowPatch as FA
        ax.plot(cx, cy, 'o', color=INK, ms=4)
        ax.add_patch(FA((cx, cy), (cx + R * .707, cy - R * .707), arrowstyle='-|>', mutation_scale=14, lw=1.6, color=ROZMER))
        ax.add_patch(FA((cx, cy), (cx - r, cy), arrowstyle='-|>', mutation_scale=14, lw=1.6, color=ROZMER))
        ax.text(cx + R * .8, cy - R * .95, txt_R, color=ROZMER, fontsize=18)
        ax.text(cx - r / 2, cy + .1, txt_r, color=ROZMER, fontsize=16, ha='center')
    else:
        kota(ax, cx - R, cy - R - .25, cx + R, cy - R - .25, txt_R, dy=-.2)
        kota(ax, cx - r, cy, cx + r, cy, '', dy=0); ax.text(cx, cy + .15, txt_r, color=ROZMER, fontsize=17, ha='center')
    ax.text(cx, cy + R + .2, 'průřez', fontsize=18, ha='center')
    if extra: ax.text(-R, -.55, extra, fontsize=18)
    ax.set_xlim(-R - .5, cx + R + 1.1); ax.set_ylim(-.9, h + 1.2)
    uloz(fig, jmeno)

def dva_materialy():
    fig, ax = start(4.5, 4.5)
    ax.add_patch(Rectangle((0, 1.2), 2, 1.1, fc='#cfe0f5', ec=INK, lw=2)); ax.text(1, 1.75, 'A', fontsize=30, ha='center', va='center')
    ax.add_patch(Rectangle((0, 0), 2, 1.2, fc='#f6d5bf', ec=INK, lw=2)); ax.text(1, .6, 'B', fontsize=30, ha='center', va='center')
    for x in np.linspace(.2, 1.8, 5):
        sila(ax, x, 3.0, x, 2.35); sila(ax, x, -.75, x, -.05)
    ax.text(2.25, 1.75, '100 MPa', fontsize=18, va='center'); ax.text(2.25, .6, '200 MPa', fontsize=18, va='center')
    ax.text(2.1, 2.75, '$F$ = ?', color=SILA, fontsize=18)
    ax.text(1, -1.1, '$S$ = 10 mm²', fontsize=18, ha='center')
    ax.set_xlim(-.4, 3.6); ax.set_ylim(-1.4, 3.2)
    uloz(fig, '037_pruznost_dva_materialy.png')

def zpereny():
    fig, ax = start(6, 3.6)
    L = 1.6 / np.tan(np.radians(30))                     # délka vlákna ve směru x
    ax.plot([0, 3.0], [0, 0], color='#c9b37a', lw=9, solid_capstyle='round')            # spodní aponeuróza + šlacha
    ax.plot([L - .2, L + 3.2], [1.6, 1.6], color='#c9b37a', lw=9, solid_capstyle='round')  # horní aponeuróza
    for x in np.linspace(L + 3.2, L + 3.2, 1):
        ax.plot([x, x], [1.3, 1.9], color=INK, lw=2.4)
        for y in np.linspace(1.3, 1.85, 5): ax.plot([x, x + .15], [y, y + .12], color=INK, lw=1.2)
    for x0 in np.linspace(.2, 2.8, 5):
        ax.plot([x0, x0 + L], [0, 1.6], color=SVAL, lw=7, solid_capstyle='round', alpha=.9)
    uhel(ax, .2, 0, .55, 0, 30)
    ax.text(.2 + .62, .1, '30°', color=ROZMER, fontsize=17)
    sila(ax, 0, 0, -1.0, 0, '$F_{sval}$ = ?', dx=-.3, dy=-.42)
    ax.text(2.6, -.55, 'fyziologický průřez 5 cm²,  σ = 1 MPa', fontsize=17, ha='center')
    ax.set_xlim(-1.6, L + 3.6); ax.set_ylim(-.95, 2.1)
    uloz(fig, '038_pruznost_zpereny_sval.png')

def slacha_valec():
    fig, ax = start(6, 3.2)
    ax.add_patch(Rectangle((-.4, -.5), .4, 1.0, fc='#cccccc', ec=INK, lw=2))
    valec(ax, 0, 3, 0, .2, fc='#f3e7d3')
    ax.plot([3, 3.25], [0, 0], color=INK, lw=2); ax.plot([3.25, 3.25], [-.2, .2], color='#999999', lw=2, ls='--')
    sila(ax, 3.25, 0, 4.1, 0, '$F$ = 13,4 N', dx=-.65, dy=.15)
    kota(ax, 0, -.45, 3, -.45, '15 cm', dy=-.18)
    kota(ax, 3, .4, 3.25, .4, '', dy=0); ax.text(3.12, .6, '3,7 mm', color=ROZMER, fontsize=17, ha='center')
    ax.text(1.5, .38, '$d$ = 8,5 mm', fontsize=18, ha='center')
    ax.set_xlim(-.6, 4.4); ax.set_ylim(-.95, .95)
    uloz(fig, '039_pruznost_modul_slachy.png')

def kost_pevnost():
    fig, ax = start(6, 3.2)
    valec(ax, 0, 3, 0, .4)
    sila(ax, 0, 0, -1.0, 0, '$F$ = ?', dx=-.1, dy=.12); sila(ax, 3, 0, 4.0, 0, '$F$ = ?', dx=-.4, dy=.12)
    ax.text(1.5, .62, '$S$ = 3 cm²', fontsize=20, ha='center')
    ax.text(1.5, -.85, '$E$ = 18 GPa,  $σ_{pt}$ = 120 MPa', fontsize=18, ha='center')
    ax.set_xlim(-1.4, 4.4); ax.set_ylim(-1.1, .95)
    uloz(fig, '042_pruznost_pevnost_kosti.png')

if __name__ == '__main__':
    kost_tah(); drat(); sval_pcsa(); vaz(); pruzina(); dva_materialy(); zpereny(); slacha_valec(); kost_pevnost()
    trubice('028_pruznost_femur_trubice.png', 1.0, .67, '$R$ = 3 cm', '$r$ = 2 cm', '$F$ = 1000 N', 'E = 200 MPa', '$l$', polomer=True)
    trubice('034_pruznost_diafyza.png', 1.0, .75, '40 mm', '30 mm', '$F$ = 2000 N', None, None)
