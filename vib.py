# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

EDO de movimento do sistema
"""
import numpy as np
from numpy.linalg import inv

def vib(t,y):
    w = 50j
    M = np.array([[2,0,0],[0,5,0],[0,0,1]])
    C = np.array([[300,-200,0],[-200,350,-150],[0,-150,150]])
    K = np.array([[12000,-8000,0],[-8000,14000,-6000],[0,-6000,6000]])
    F = np.array([[0],[50*np.exp(w*t)],[0]])

    n = len(F)
    aux = np.zeros((3,3))
    aux2 = np.identity(3)

    aux3 = -inv(M).dot(K)
    aux4 = -inv(M).dot(C)
    aux5 = inv(M).dot(F)
    
    aux6 = np.zeros((n,1))
    
    A = np.block([[aux,aux2],[aux3,aux4]])
    auxq = np.block([[aux6],[aux5]])
    Q = np.reshape(auxq,(len(auxq),))
    
    dy = A.dot(y) + Q
    print(dy)
    return dy
