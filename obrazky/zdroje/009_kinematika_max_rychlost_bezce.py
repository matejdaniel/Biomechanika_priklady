from styl import *
fig, ax = start(6.4, 4, osy=True)
t = [0, 10, 20, 30, 40]; x = [0, 9, 9, 12, 2]
ax.plot(t, x, color=SILA)
ax.set_xlabel('t [s]'); ax.set_ylabel('x [m]')
ax.set_xlim(0, 42); ax.set_ylim(0, 14); ax.set_xticks(t); ax.set_yticks(range(0, 15, 2))
graf(ax)
uloz(fig, '009_kinematika_max_rychlost_bezce.png')
