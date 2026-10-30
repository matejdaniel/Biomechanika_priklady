"""021 – Platnost Hookeova zákona: diagram napětí–deformace šlachy s úseky A–D + motiv lýtka a Achillovy šlachy (z 001)."""
from styl import *
import numpy as np
from pp_grafy1 import kval
from pp_grafy2 import krivka
from importlib import import_module
motiv = import_module("001_pruznost_modul_slachy").motiv

if __name__ == '__main__':
    fig, ax = start(6, 4, osy=True)
    krivka(ax, [0, 1, 1.9, 2.1], [0, .15, .45, .6], color=SILA)
    ax.plot([2.1, 3.6], [.6, 5.0], color=SILA)
    krivka(ax, [3.6, 3.9, 4.5, 6.6], [5.0, 5.45, 5.6, 5.6], color=SILA)
    krivka(ax, [6.6, 6.8, 7.4, 8.1], [5.6, 5.4, 4.3, 2.4], color=SILA)
    for xv in (2.1, 3.75, 6.6): ax.axvline(xv, color=ROZMER, lw=1.1, ls='--', alpha=.6)
    for (xc, t) in [(1.05, 'A'), (2.9, 'B'), (5.2, 'C'), (7.6, 'D')]:
        ax.text(xc, 6.4, t, fontsize=22, ha='center', color=ROZMER)
    ax.set_xlim(0, 13.5); ax.set_ylim(0, 7.2)
    kval(ax, 'poměrná deformace ε', 'napětí σ')
    ins = ax.inset_axes([0.62, 0.02, 0.4, 0.78]); motiv(ins)
    uloz(fig, '021_pruznost_hooke.png')
