import numpy as np

def nfA(vecx):
    n = len(vecx)
    a = lambda i,j : np.prod([vecx[i]-vecx[k] for k in range(j)])
    return np.array([[a(i,j) for j in range(n)] for i in range(n)])
