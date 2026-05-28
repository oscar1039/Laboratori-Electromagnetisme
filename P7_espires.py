import matplotlib.pyplot as plt
import numpy as np


mu_0 = 4*np.pi *10**(-2)

def B(r,n):
    return 2*mu_0*n/r

N=1000

radis=np.linspace(2.5,6.5,N)
nombre=np.linspace(0.5,3.5,N)

r_exp=[3,4.25,6]
u_r=[0.05,0.05,0.05]
b_exp_1=[0.09,0.06,0.043]
n_exp=[1,2,3]
u_n=[0,0,0]
b_exp_2=[0.043,0.085,0.123]
u_b=[0.01,0.01,0.01]

camp1=[]
camp2=[]


for i in range(len(radis)):
    camp1.append(B(radis[i],1))

for i in range(len(nombre)):
    camp2.append(B(6,nombre[i]))




def graf_res(x,y,ux,uy,xtit,ytit,colorin,labelin):
    
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    ux = np.array(ux, dtype=float)
    uy = np.array(uy, dtype=float)
    
    plt.errorbar(x, y, xerr=ux, yerr=uy, capsize=3, elinewidth=1.5 ,fmt="o", color=colorin, label=labelin)
    plt.tight_layout()
    plt.axis('auto')
    plt.autoscale(True)  # Activa el ajuste automático de los ejes
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.minorticks_on()
    plt.tick_params(which='both', direction='in', right=True, top=True)
    plt.xlabel(xtit,fontsize=12)
    plt.ylabel(ytit,fontsize=12)
    plt.legend()
    plt.legend(loc='best', fontsize=10)
    plt.box(on=True)

plt.plot(radis,camp1,label="Camp teòric")
graf_res(r_exp,b_exp_1,u_r,u_b,"R (cm)","B (mT)","red","mesures")
plt.show()

plt.plot(nombre,camp2,label="Camp teòric")
graf_res(n_exp,b_exp_2,u_n,u_b,"N","B (mT)","red","mesures")
plt.show()
