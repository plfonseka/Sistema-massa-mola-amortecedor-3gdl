# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

Resposta Temporal do Sistema
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp 
from vib import vib

x0 = np.array([[0],[0],[0]])
xp0 = np.array([[0],[0],[0]])
aux = np.block([[x0],[xp0]])
y0 = np.reshape(aux,(len(aux),))

tin = 0
tf = 10

sol = solve_ivp(vib,[tin,tf],y0);

T = sol.t
Y = sol.y

dof = len(x0)
x = Y[0:dof,:]
xp = Y[dof:2*dof,:]

#for i in range(dof):
#    plt.plot(T, x[i,:])  # Plot some data on the (implicit) axes.
#    plt.xlabel('Tempo $(t)$')
#    plt.ylabel('Amplitude')
#    plt.title("Resposta temporal (Deslocamento)")
       
plt.plot(T, xp[0,:], color='b', label='GL3')  # Plot some data on the (implicit) axes.
plt.xlabel('Tempo $(t)$')
plt.ylabel('Amplitude')
plt.title('RESPOSTA TEMPORAL (Deslocamento)')   

#plt.savefig('freq_acima50.png',dpi=1200)

    


