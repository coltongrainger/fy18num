#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import numpy as np
from numpy import pi, cos, sin, sqrt
import scipy

f = lambda t: np.sin(pow(np.pi*t,0.5))
F = lambda t: -2*(sqrt(pi)*sqrt(t)*cos(sqrt(pi)*sqrt(t)) - sin(sqrt(pi)*sqrt(t)))/pi

vecx = lambda n,a,b: np.linspace(a,b,n+1)
intervals = [(0.,1.),(np.pi/4,9*np.pi/4),(np.pi,2*np.pi)]

quadrat = lambda n,r: trapz(f(vecx(2**n,*r)),vecx(2**n,*r))
exact = lambda a,b: F(b) - F(a)
error = lambda n,r: exact(*r) - quadrat(n,r)

p5 = np.array([[error(n,r) for n in range(20)]\
               for r in intervals], dtype=float)

