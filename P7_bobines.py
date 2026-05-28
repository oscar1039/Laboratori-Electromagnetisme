import matplotlib.pyplot as plt
import numpy as np

N=1000
mu_0 = 4*np.pi *10**(-2)    # mT·cm/A

def B(n,l,r,z):
    return (mu_0*n/(2*l))*((z+l/2)/(np.sqrt(r**2+(z+l/2)**2))-(z-l/2)/(np.sqrt(r**2+(z-l/2)**2)))

r_exp=[9.5,
7.5,
5.5,
3.5,
1.5,
-0.5,
-2.5,
-4.5,
-6.5,
-8.5,
-9.5]

camp_exp1=[0.35,
1.46,
2.06,
2.21,
2.24,
2.25,
2.26,
2.22,
2.01,
1.06,
0.5]
camp_exp2=[0.05,
0.3,
0.56,
0.6,
0.61,
0.61,
0.61,
0.59,
0.55,
0.25,
0.1]
camp_exp3=[0.14,
0.8,
1.12,
1.19,
1.2,
1.21,
1.18,
1.18,
1.08,
0.43,
0.17]
camp_exp4=[0.3,
1.62,
2.22,
2.29,
2.31,
2.31,
2.31,
2.26,
2.06,
0.78,
0.3]

zz=np.linspace(-10,10,N)    # cm
ur=[]
ub=[]
for i in range(len(r_exp)):
    ur.append(0.2)
    ub.append(0.02)

camp1=B(300,16,3.3/2,zz)    # mT

camp2=B(75,16,2.6/2,zz)
camp3=B(150,16,2.6/2,zz)
camp4=B(300,16,2.6/2,zz)

def graf_res(x,y,ux,uy,xtit,ytit,colorin,labelin):
    
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    ux = np.array(ux, dtype=float)
    uy = np.array(uy, dtype=float)
    
    plt.errorbar(x, y, xerr=ux, yerr=uy, capsize=2.5, elinewidth=1 ,fmt=".", color=colorin, label=labelin)
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

plt.plot(zz,camp1,label="Camp teòric 1")
graf_res(r_exp,camp_exp1,ur,ub,"z (cm)","B (mT)","red","mesures bobina 1")
plt.show()

plt.plot(zz,camp2,color="red")
graf_res(r_exp,camp_exp2,ur,ub,"z (cm)","B (mT)","red","mesures bobina 2")

plt.plot(zz,camp3,color="purple")
graf_res(r_exp,camp_exp3,ur,ub,"z (cm)","B (mT)","purple","mesures bobina 3")

plt.plot(zz,camp4,color="blue")
graf_res(r_exp,camp_exp4,ur,ub,"z (cm)","B (mT)","blue","mesures bobina 4")
plt.show()
