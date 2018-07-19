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
