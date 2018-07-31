#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from sympy import Piecewise

def natcubic_hardcoded(x):
    h = 0.5; vecx = [0.,0.5,0.]
    a = [0,1,0]
    c = [0,-3/(2*h**2),0]
    d = [-1/(2*h**3), 1/(2*h**3)]
    b = [3/(2*h), 0]
    terms = lambda x,i: a[i]+b[i]*(x-vecx[i])\
                         +c[i]*(x-vecx[i])**2\
                         +d[i]*(x-vecx[i])**3
    spline = Piecewise((terms(x,0), 0<=x<0.5),(terms(x,1),0.5<=x<=1))
    return spline

def natcubic_hardcoded_terms(x,i):
    h = 0.5; vecx = [0.,0.5,0.]
    a = [0,1,0]
    c = [0,-3/(2*h**2),0]
    d = [-1/(2*h**3), 1/(2*h**3)]
    b = [3/(2*h), 0]
    terms = lambda x,i: a[i]+b[i]*(x-vecx[i])\
                         +c[i]*(x-vecx[i])**2\
                         +d[i]*(x-vecx[i])**3
    return terms(x,i)

s0 = natcubic_hardcoded_terms(x,0)
s1 = natcubic_hardcoded_terms(x,1)
ds0 = sym.diff(s0,x)
ds1 = sym.diff(s1,x)
d2s0 = sym.diff(s0,x,2)
d2s1 = sym.diff(s1,x,2)

print(s0.subs(x,0.5) == s1.subs(x,0.5))
print(ds0.subs(x,0.5) == ds1.subs(x,0.5))
print(d2s0.subs(x,0.5) == d2s1.subs(x,0.5))
print(d2s0.subs(x,0),d2s1.subs(x,1))
