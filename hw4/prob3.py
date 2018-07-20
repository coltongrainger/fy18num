def lagrange_basis(vecx):
    # how many points?
    n = len(vecx)
    # choose n-1 of n entries
    hinges = [np.concatenate([vecx[:i], vecx[i+1:]]) for i in range(n)]
    # take product of n-1 terms, format into lambda functions
    polys = [lambda t, i=i: np.prod((t-hinges[i])/(vecx[i]-hinges[i]))\
            for i in range(n)]
    return polys

def lagrange_basis_plot(vecx):
    polys = lagrange_basis(vecx)
    start, stop = np.min(vecx), np.max(vecx)
    stiple = np.linspace(start,stop)
    return [plt.plot(stiple,[polys[i](t) for t in stiple])\
            for i in range(len(vecx))]

def lagrange_coords(f,vecx):
    return np.array([f(x) for x in vecx])

def interpol(coords,polys,t):
    scale = [lambda p, a=a: p * a for a in coords]
    return sum([scale[i](polys[i](t)) for i in range(len(vecx))])

def newton_basis(vecx):
    return

dd = lambda f, vecx: ((dd(f,vecx[1:])-dd(f,vecx[:-1]))/(vecx[-1]-vecx[0]) if len(vecx)>1 else f(vecx[0]))
