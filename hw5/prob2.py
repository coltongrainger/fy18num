#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import numpy as np

x=np.array([0.0, 0.5, 1.0, 1.5, 1.7, 1.85, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 5.75, 6.0])
y=np.array([0.0, 0.9, 1.2, 1.35, 1.4, 1.7, 1.95, 2.3, 2.35, 2.4, 2.35, 2.25, 1.8, 1.0, 0.7, 0.0])
v=np.array([0.0, 0.5, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0])
w=np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.45, 0.6, 0.45, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.45, 0.6, 0.45, 0.0, 0.0, 0.0, 0.0, 0.0])

from scipy.interpolate import CubicSpline, lagrange
ptop=lagrange(x,y)
pbot=lagrange(v,w)
ctop=CubicSpline(x,y)
cbot=CubicSpline(v,w)

import matplotlib.pyplot as plt
stip = np.linspace(0,6, 500)
plt.plot(stip,ptop(stip), color="Red")
plt.plot(stip,pbot(stip), color="Orange")
plt.scatter(x,y, color="Black")
plt.scatter(v,w, color="Black")
plt.axis([-0.5,6.5,-0.5,3])
plt.ylabel("Buggy height")
plt.title("Minimal degree polynomial interpolation")
plt.grid()
plt.show()

plt.plot(stip,ctop(stip), color="Red")
plt.plot(stip,cbot(stip), color="Orange")
plt.scatter(x,y, color="Black")
plt.scatter(v,w, color="Black")
plt.axis([-0.5,6.5,-0.5,3])
plt.title("Cubic spline (not-a-knot) interpolation")
plt.ylabel("Buggy height")
plt.grid()
plt.show()
