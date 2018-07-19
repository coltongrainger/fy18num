import numpy as np

def jacobi(A,b,x0, *args):
    U = np.triu(A,1)
    D = np.diag(A)
    L = np.tril(A,-1)
    x1 = (1/D) * (b - np.matmul((L+U),x0))
    return x1, np.linalg.norm(x1 - x0, ord=np.inf)

def gauss_seidel(A,b,x0, *args):
    n = len(x0)
    x1=np.zeros(n)
    for i in range(n):
        new = np.sum(A[i,:i] * x1[:i])
        old = np.sum(A[i,i+1:] * x0[i+1:])
        x1[i] = (1 / A[i,i]) * (b[i] - new - old)
        # print(A[i,:i],x1[:i]," has inner product new ",new)
        # print(A[i,i+1:],x0[i+1:]," has inner product old ",old)
        # print(1/A[i,i],"(",b[i]," less new less old) is ",x1[i])
    return x1, np.linalg.norm(x1 - x0, ord=np.inf)

def SOR(A,b,x0,omega):
    n = len(x0)
    x1=np.zeros(n)
    for i in range(n):
        jaterm = (1-omega) * x0[i]
        gsnew = np.sum(A[i,:i] * x1[:i])
        gsold = np.sum(A[i,i+1:] * x0[i+1:])
        gsterm = (omega / A[i,i]) * (b[i] - gsnew - gsold)
        x1[i] = jaterm + gsterm
    return x1, np.linalg.norm(x1-x0, ord=np.inf)

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def capture_error(method,A,b,x_approx,omega,x_exact,eps):
    error = np.array([np.linalg.norm(x_approx - x_exact, ord=np.inf)])
    while error[-1] > eps:
        x_approx = method(A,b,x_approx,omega)[0]
        error = np.append(error, np.linalg.norm(x_approx - x_exact, ord=np.inf))
    return error
