import sympy as sym

def hermite_basis(vecx):
    lp = lagrange_basis(vecx)
    dp = [l(sym.Symbol('x')).diff(x) for l in lp]
    hf = [lambda t, i=i:\
            (1-2*dp[i].subs(x,vecx[i])*(t-vecx[i]))*lp[i](t)\
            for i in range(len(vecx))]
    hh = [lambda t, i=i: (t-vecx[i])*(lp[i])**2\
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
    sum([scale[i](polys[i](t)) for i in range(len(polys))])
