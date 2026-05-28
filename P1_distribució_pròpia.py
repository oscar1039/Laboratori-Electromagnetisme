import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

x = np.linspace(0, 2.5, 400)
y = np.linspace(0, 2, 400)
X, Y = np.meshgrid(x, y)

a, b = 0.8, 0.7
q = 1.0

charges = [
    ( q,  a,  b),
    (-q, -a,  b),
    (-q,  a, -b),
    ( q, -a, -b)
]

V = np.zeros_like(X)
for qi, xi, yi in charges:
    R2 = (X-xi)**2 + (Y-yi)**2 + 1e-6
    V += qi * np.log(np.sqrt(R2))

Ey, Ex = np.gradient(-V, y, x)

fig, ax = plt.subplots()

ax.streamplot(X, Y, Ex, Ey, density=0.8,color="black",arrowsize=0.8,linewidth=0.8)
ax.contour(X, Y, V, levels=16,colors="tab:blue",linestyles='solid',linewidths=0.8)

plt.axvline(0,0,1, color='red',linewidth=4)
plt.axhline(0,0,1, color='red',linewidth=4)

plt.scatter([a], [b], color='blue',s=50,zorder=10)

legend_elements = [
    Line2D(
        [0], [0],
        marker='>',
        color='black',
        markerfacecolor='black',
        markersize=3,
        lw=0.8,
        label='Línies camp elèctric'
    ),
    Line2D(
        [0], [0],
        color='tab:blue',
        lw=0.8,
        label='Línies equipotencials'
    ),

    Line2D(
        [0], [0],
        color='red',
        lw=3,
        label='Electrode positiu'
    ),

    Line2D(
        [0], [0],
        marker='o',
        color='w',
        markerfacecolor='blue',
        markersize=6,
        label='Electrode negatiu'
    )
]

plt.xlabel('x (cm)',fontsize=10)
plt.ylabel('y (cm)',fontsize=10)
plt.legend(handles=legend_elements,loc="center left",bbox_to_anchor=(0.7,0.9), fontsize=7.5)

plt.tight_layout()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.minorticks_on()
plt.tick_params(which='both', direction='in', right=True, top=True)
plt.box(on=True)

ax.set_aspect('equal')
ax.set_xlim(-0.01, 2.5)
ax.set_ylim(-0.01, 2)

plt.show()
