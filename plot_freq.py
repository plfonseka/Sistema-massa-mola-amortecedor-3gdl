# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

Resposta em Frequência do Sistema
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt  
import vibration_toolbox as vbt

m1,m2,m3 = 2,5,1
k1,k2,k3 = 4000,8000,6000
c1,c2,c3 = 100,200,150

M = np.array([[m1,0,0],
              [0,m2,0],
              [0,0,m3]])
C = np.array([[c1+c2,-c2,0],
              [-c2,c2+c3,-c3],
              [0,-c3,c3]])
K = np.array([[k1+k2,-k2,0],
              [-k2,k2+k3,-k3],
              [0,-k3,k3]])

def plot_freq_resp(self, modes=None, ax0=None, ax1=None, **kwargs):
    
    if ax0 is None or ax1 is None:
        fig, ax = plt.subplots(2)
        if ax0 is not None:
            _, ax1 = ax
        if ax1 is not None:
            ax0, _ = ax
        else:
            ax0, ax1 = ax

    omega, magdb, phase = self.freq_response(modes=modes)
    omeg = np.linspace(0,100,1000)
    
    for i in range(3):
        ax0.plot(omeg, magdb[2, i, :], **kwargs)
        ax1.plot(omeg, phase[2, i, :], **kwargs)
    
    for ax in [ax0, ax1]:
        ax.set_xlim(0, max(omeg))
        ax.yaxis.set_major_locator(
            mpl.ticker.MaxNLocator(prune='lower'))
        ax.yaxis.set_major_locator(
            mpl.ticker.MaxNLocator(prune='upper'))
    
#    for i in range(3):
#        for j in range(3):
#            ax0.plot(omeg, magdb[i, j, :], **kwargs)
#            ax1.plot(omeg, phase[i, j, :], **kwargs)
#        for ax in [ax0, ax1]:
#            ax.set_xlim(0, max(omeg))
#            ax.yaxis.set_major_locator(
#                mpl.ticker.MaxNLocator(prune='lower'))
#            ax.yaxis.set_major_locator(
#                mpl.ticker.MaxNLocator(prune='upper'))

    ax0.set_ylabel('Magnitude $(dB)$')
    ax1.set_ylabel('Ângulo de Fase $(°)$')
    ax1.set_xlabel('Frequência (rad/s)')

    return ax0, ax1

sys = vbt.VibeSystem(M,C,K)

plot_freq_resp(sys)
#plt.savefig('frf_3.png',dpi=1200)



