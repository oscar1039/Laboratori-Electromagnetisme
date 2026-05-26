import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

L = 2.0
d = 1.0
sigma = 1.0

Ny = 200
z_prime = np.linspace(-L/2, L/2, Ny)
x=np.full(Ny,d/2)
x_prime=np.full(Ny,-d/2)
dz = z_prime[1] - z_prime[0]

y = np.linspace(-2, 2, 200)
z = np.linspace(-2, 2, 200)
Y, Z = np.meshgrid(y, z)

Ey = np.zeros_like(Y)
Ez = np.zeros_like(Z)
V = np.zeros_like(Z)

for zp in z_prime:
    Ry = Y - d/2
    Rz = Z - zp
    R2 = Ry**2 + Rz**2 + 1e-6
    Ey -= sigma * Ry / R2 * dz
    Ez -= sigma * Rz / R2 * dz
    V -= sigma * np.log(np.sqrt(R2)) * dz

    Ry = Y +d/2
    Rz = Z -zp
    R2 = Ry**2 + Rz**2 + 1e-6
    Ey += sigma * Ry / R2 * dz
    Ez += sigma * Rz / R2 * dz
    V += sigma * np.log(np.sqrt(R2)) * dz


plt.streamplot(Y, Z, Ey, Ez,color="black", density=0.8,linewidth=0.8,arrowsize=0.8)
plt.contour(Y, Z, V, levels=20,colors="tab:blue",linestyles='solid',linewidths=0.8)

plt.plot(x,z_prime, color='blue',linewidth=4)
plt.plot(x_prime,z_prime, color='red',linewidth=4)

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
        color='blue',
        lw=3,
        label='Placa negativa'
    ),

    Line2D(
        [0], [0],
        color='red',
        lw=3,
        label='Placa positiva'
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

plt.show()