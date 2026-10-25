"""002 – Mumie: ilustrace z Gemini (002_skalovani_mumie_ilustrace.png) + kóty.
Malá mumie je zmenšena přesně na polovinu výšky velké (izometrické škálování 1 m : 2 m)."""
from styl import *
from PIL import Image
import numpy as np

ILU = '002_skalovani_mumie_ilustrace.png'
a = np.asarray(Image.open(ILU).convert('RGB')).astype(np.uint8)
H, W, _ = a.shape

# 1) čisté bílé pozadí (stín z Gemini nahrazuje kreslená čára země)
bg = np.full_like(a, 255)

def vyrez(x0, x1, y0, y1):
    sub = a[y0:y1, x0:x1]
    alfa = (np.abs(sub.astype(int) - 255).sum(2) > 45).astype(np.uint8) * 255
    # spodní řádky: ponech jen pixely mezi obrysy chodidel (odstraní stín z Gemini)
    for r in range(sub.shape[0] - 90, sub.shape[0]):
        tmave = np.where(sub[r].mean(1) < 110)[0]
        if len(tmave) == 0: alfa[r] = 0; continue
        alfa[r, :tmave.min()] = 0; alfa[r, tmave.max() + 1:] = 0
    rgba = np.dstack([sub, alfa])
    return Image.fromarray(rgba, 'RGBA')

maly  = vyrez(797, 1086, 600, 1545)            # chodidla malé mumie v y = 1551
velky = vyrez(1350, 1775, 130, 1550)           # chodidla velké mumie v y = 1556
h_velky = 1556 - 139
k = (h_velky / 2) / (1551 - 607)               # zmenšení malé mumie na polovinu výšky velké
maly = maly.resize((round(maly.width * k), round(maly.height * k)), Image.LANCZOS)

out = Image.fromarray(bg).convert('RGBA')
out.alpha_composite(velky, (1350, 130))
x_m = 1086 - maly.width                         # pravý okraj zůstává na místě
out.alpha_composite(maly, (x_m - 60, 1545 - maly.height))
ilu = np.asarray(out.convert('RGB'))

# 2) kóty a popisky
fig, ax = start(6, 4)
ax.imshow(ilu, extent=(0, W, H, 0)); ax.set_xlim(250, 2280); ax.set_ylim(1700, 40)
pata = 1553
top_m = pata - h_velky / 2; top_v = 139
cx_m, cx_v = 880, 1563                          # středy postav
ax.plot([350, 2150], [pata, pata], color=INK, lw=1.4, alpha=.45)
kota(ax, 680, pata, 680, top_m, '', dy=0)
ax.text(600, (pata + top_m) / 2, '1 m', color=ROZMER, fontsize=22, ha='right', va='center')
kota(ax, 1880, pata, 1880, top_v, '', dy=0)
ax.text(1960, (pata + top_v) / 2, '2 m', color=ROZMER, fontsize=22, ha='left', va='center')
ax.text(cx_m, 1650, '15 m obinadla', fontsize=18, ha='center', va='center')
ax.text(cx_v, 1650, '? m obinadla', fontsize=18, ha='center', va='center')
ax.text(330, 200, 'šířka obinadla 20 cm', fontsize=20, ha='left')
uloz(fig, '002_skalovani_mumie.png')
