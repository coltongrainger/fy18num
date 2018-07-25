import numpy as np
import matplotlib.pyplot as plt

def w(vecx, x): 
    return np.product(vecx - x)

def chebyshev_transform(vecx):
    n = len(vecx) - 1
    return -1*np.cos(vecx*(np.pi/2)*n/(n+1) + np.pi/2)

def w_plot(vecx):
    stiple = np.linspace(-1,1,100)
    w_values = np.array([w(vecx, i) for i in stiple])
    return plt.plot(stiple,w_values)

def w_contrast(vecx):
    return w_plot(vecx), w_plot(chebyshev_transform(vecx))
