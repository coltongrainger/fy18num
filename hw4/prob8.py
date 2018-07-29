import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

def hermite_basis(vecx):
    lp = lagrange_basis(vecx)
    # appealing to sympy for differentiation
    # TODO implement numerically and avoid calling .evalf()
    dp = [l(sym.Symbol('x')).diff(x) for l in lp]
    hf = [lambda t, i=i:\
            (1-2*dp[i].subs(x,vecx[i])*(t-vecx[i]))*lp[i](t)\
            for i in range(len(vecx))]
    hh = [lambda t, i=i:\
            (t-vecx[i])*(lp[i](t))**2\
            for i in range(len(vecx))]
    return [hf,hh]

def lagherm_coords(f,vecx):
    vecf = [f(vecx[i]) for i in range(len(vecx))]
    df = lambda t: f(sym.Symbol('x')).diff(x).subs(x,t)
    vecdf = [df(vecx[i]) for i in range(len(vecx))]
    return [np.array(vecf), np.array(vecdf)]

# TODO rewrite hermite_basis & lagherm_coords to
# avoid flattening their outputs
flatten = lambda l: [item for sublist in l for item in sublist]

def lagherm_interpol(lagherm_coords, hermite_basis, t):
    coords = flatten(lagherm_coords)
    polys = flatten(hermite_basis)
    scale = [lambda p, a=a: p * a for a in coords]
    return sum([scale[i](polys[i](t)) for i in range(len(polys))])

# specific test case
x = sym.Symbol('x')
f = lambda x: x*sym.log(x)
vecx = np.array([1,3])

# hermite interpolating cubic poly
coordinates = lagherm_coords(f,vecx)
basis = hermite_basis(vecx)
p = lambda t: lagherm_interpol(coordinates, basis, t)
stiple = np.linspace(1,3)
pstiple = [p(t) for t in stiple]
plt.plot(stiple,pstiple)
plt.show()

# linear interpolant
m = (f(3) - f(1))/2
line = lambda x: m*(x-1)
lstiple = line(stiple)
plt.plot(stiple,lstiple)
plt.show()

# error
def hermite_error_bound(f, vecx):
    w = lambda x: np.prod([(x-i)**2 for i in vecx])
    # extreme values of cts diff'ble func on compact set
    # we assume vecx includes endpoints of compact set
    extrema = sym.solve(sym.diff(w(sym.Symbol('x')),x),x) + [w(i) for i in vecx]
    worst_wiggle = max([abs(w(x)) for x in extrema])
    jerk = sym.diff(f(sym.Symbol('x')),x,2*len(vecx))
    # assume $f^{(2n+n)}$ is monotone and find extrema at endpoints
    worst_jerk = max([jerk.subs(x,i) for i in vecx])
    return worst_jerk * worst_wiggle / sym.factorial(len(vecx))
