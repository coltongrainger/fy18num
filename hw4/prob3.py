def lagrange_basis(vecx):
    n = len(vecx)
    # choose n-1 of n entries
    hinges = [np.concatenate([vecx[:i], vecx[i+1:]]) for i in range(n)]
    # take product of n-1 terms, format into lambda functions
    polys = [lambda t, i=i: np.prod((t-hinges[i])/(vecx[i]-hinges[i]))\
            for i in range(n)]
    # returns a list of n functions, the Lagrange basis polynomials
    return polys

def lagrange_basis_plot(vecx):
    polys = lagrange_basis(vecx)
    start, stop = np.min(vecx), np.max(vecx)
    stiple = np.linspace(start,stop)
    # returns a list of plots of the basis polynomials, overlaid
    return [plt.plot(stiple,[polys[i](t) for t in stiple])\
            for i in range(len(vecx))]

def lagrange_coords(f,vecx):
    # returns the n coordinates of the interpolating polynomial
    # as a vector in $\mathcal{P}_n$ with the Lagrange basis
    return np.array([f(x) for x in vecx])

def interpol(coords,polys,t):
    # scales each vector by its coordinate
    scale = [lambda p, a=a: p * a for a in coords]
    # sums to form the desired linear combination
    # returns a (floating point) scalar
    return sum([scale[i](polys[i](t)) for i in range(len(vecx))])

def newton_basis(vecx):
    n = len(vecx)
    # returns a list of n functions, the newton form basis polynomials
    return [lambda t, j=j: np.prod([t-vecx[i] for i in range(j)])\
            for j in range(n)]

def newton_basis_plot(vecx):
    polys = newton_basis(vecx)
    start, stop = np.min(vecx), np.max(vecx)
    stiple = np.linspace(start,stop)
    # returns a list of plots of the basis polynomials, overlaid
    return [plt.plot(stiple,[polys[i](t) for t in stiple])\
            for i in range(len(vecx))]

def dd(f, vecx):
    if len(vecx)>1:
    # recursive call, returns the coordinate of the nth newton poly
        return (dd(f,vecx[1:]) - dd(f,vecx[:-1]))/(vecx[-1]-vecx[0])
    # floor of recursion
    else:
        return f(vecx[0])

def newton_coords(f, vecx):
    # TODO: save the recursive divided difference calls in memory
    # so we don't have to iterate to load them into this array
    return np.array([dd(f,vecx[:i+1]) for i in range(len(vecx))])


