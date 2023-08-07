# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

Autovalores e Autovetores do Sistema
"""
import numpy as np
from numpy.linalg import inv
import scipy.linalg as la

M = np.array([[2,0,0],[0,5,0],[0,0,1]])
C = np.array([[300,-200,0],[-200,350,-150],[0,-150,150]])
K = np.array([[12000,-8000,0],[-8000,14000,-6000],[0,-6000,6000]])

aux = np.zeros((3,3))
aux2 = np.identity(3)

aux3 = -inv(M).dot(K)
aux4 = -inv(M).dot(C)

A = np.block([[aux,aux2],[aux3,aux4]])

w,vl,vr = la.eig(A,left=True);

eigvals=np.around(np.diag(w),4)
eigvect=np.around(vl,4)

print(eigvals,eigvect)