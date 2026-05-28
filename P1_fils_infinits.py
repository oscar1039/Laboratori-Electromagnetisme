import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

epsilon0 = 8.854e-12
lam = 1.0                 # densidad lineal de carga
a = 4.0                   # m

# -----------------------------
# Malla de puntos
# -----------------------------
x = np.linspace(-14, 14, 700)
y = np.linspace(-10, 10, 500)

X, Y = np.meshgrid(x, y)

# -----------------------------
# Distancias a cada hilo
# -----------------------------
r_plus_sq  = (X + a)**2 + Y**2
r_minus_sq = (X - a)**2 + Y**2

# Evitar divisiones por cero
r_plus_sq[r_plus_sq == 0] = 1e-12
r_minus_sq[r_minus_sq == 0] = 1e-12

# -----------------------------
# Campo eléctrico
# -----------------------------
coef = lam / (2 * np.pi * epsilon0)

Ex = coef * (
    (X + a)/r_plus_sq -
    (X - a)/r_minus_sq
)

Ey = coef * (
    Y/r_plus_sq -
    Y/r_minus_sq)

# -----------------------------
# Potencial eléctrico
# -----------------------------
r_plus  = np.sqrt(r_plus_sq)
r_minus = np.sqrt(r_minus_sq)

V = coef * np.log(r_minus / r_plus)

# -----------------------------
# Gráfica
# -----------------------------
fig, ax = plt.subplots()

# Equipotenciales
nivells = np.linspace(-5e10, 5e10, 16)
cont = ax.contour(X, Y, V, levels=nivells,colors="blue",linestyles='solid',linewidths=0.8)


norm = np.sqrt(Ex**2 + Ey**2)
Ex_plot = Ex / norm
Ey_plot = Ey / norm

ax.streamplot(
    X, Y,
    Ex_plot, Ey_plot,
    color='black',
    linewidth=0.8,
    density=0.7,
    arrowsize=0.8
)

legend_elements = [
    Line2D(
        [0], [0],
        color='black',
        marker='>',
        markerfacecolor='black',
        markersize=3,
        lw=0.8,
        label='Línies camp elèctric'
    ),
    Line2D(
        [0], [0],
        color='blue',
        lw=0.8,
        label='Línies equipotencials'
    ),

    Line2D(
        [0], [0],
        marker='o',
        color='w',
        markerfacecolor='red',
        markersize=6,
        label='Fil positiu'
    ),

    Line2D(
        [0], [0],
        marker='o',
        color='w',
        markerfacecolor='blue',
        markersize=6,
        label='Fil negatiu'
    )
]


# Hilos cargados
ax.plot(-a, 0, 'ro', markersize=5)
ax.plot(+a, 0, 'bo', markersize=5)

# Estética
ax.set_xlim(-14,14)
ax.set_ylim(-10,10)
ax.set_aspect('equal')

ax.set_xlabel('x (cm)',fontsize=10)
ax.set_ylabel('y (cm)',fontsize=10)
ax.legend(handles=legend_elements,loc="center left",bbox_to_anchor=(0.7,0.9), fontsize=7.5)

plt.tight_layout()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.minorticks_on()
plt.tick_params(which='both', direction='in', right=True, top=True)
plt.box(on=True)

plt.show()
