"""Jednotný kreslený styl obrázků sbírky. Použití:  from styl import *"""
import os
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import FancyArrowPatch, Arc

_FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Caveat-Regular.ttf')
fm.fontManager.addfont(_FONT)

# --- barvy (význam je pevný, viz STYL.md) ---
INK    = '#222222'  # obrysy, osy, text
SILA   = '#d62828'  # síly
MOMENT = '#f77f00'  # momenty
POHYB  = '#7b2cbf'  # rychlost, zrychlení
ROZMER = '#1d6fd1'  # kóty, úhly, vzdálenosti
BOD    = '#2a9d4b'  # těžiště, body, osy otáčení
KOST, SVAL, KUZE, DREVO = '#f1e3c8', '#e07a7a', '#f6d5bf', '#8b5a2b'

W, H, DPI = 6.0, 4.0, 200   # 1200 x 800 px

def start(w=W, h=H, osy=False):
    plt.xkcd(scale=0.8, length=120, randomness=2)
    plt.rcParams.update({
        'font.family': ['Caveat', 'DejaVu Sans'], 'font.size': 20,
        'mathtext.fontset': 'custom', 'mathtext.rm': 'Caveat',
        'mathtext.it': 'Caveat', 'mathtext.bf': 'Caveat',
        'axes.linewidth': 1.8, 'lines.linewidth': 2.4, 'path.effects': [],
        'axes.edgecolor': INK, 'text.color': INK, 'axes.labelcolor': INK,
        'xtick.color': INK, 'ytick.color': INK})
    fig, ax = plt.subplots(figsize=(w, h), dpi=DPI)
    if not osy:
        ax.set_aspect('equal'); ax.axis('off')
    return fig, ax

def graf(ax):
    """Úprava os pro grafy: bez horního a pravého rámečku, jemná mřížka."""
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.grid(alpha=.25)

def sila(ax, x0, y0, x1, y1, text=None, barva=SILA, dx=.05, dy=.05):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>',
                 mutation_scale=18, lw=2.2, color=barva))
    if text: ax.text(x1 + dx, y1 + dy, text, color=barva, fontsize=20)

def kota(ax, x0, y0, x1, y1, text, dx=0, dy=-.15):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='<->',
                 mutation_scale=14, lw=1.6, color=ROZMER))
    ax.text((x0 + x1) / 2 + dx, (y0 + y1) / 2 + dy, text, color=ROZMER,
            fontsize=18, ha='center', va='center')

def bod(ax, x, y, text=None, dx=.06, dy=.06):
    ax.plot(x, y, 'o', color=BOD, ms=9)
    if text: ax.text(x + dx, y + dy, text, color=BOD, fontsize=20)

def uhel(ax, x, y, r, od, do, text=None):
    ax.add_patch(Arc((x, y), 2 * r, 2 * r, theta1=od, theta2=do, color=ROZMER, lw=1.6))
    if text:
        import math; s = math.radians((od + do) / 2)
        ax.text(x + 1.35 * r * math.cos(s), y + 1.35 * r * math.sin(s), text,
                color=ROZMER, fontsize=18, ha='center', va='center')

def uloz(fig, jmeno):
    fig.tight_layout()
    fig.savefig(jmeno, facecolor='white', dpi=DPI)
    plt.close(fig)
