import numpy as np

def f1(x): 
    return abs(x)

def f2(x): 
    return -1 if x<0 else 1 if x>0 else 0

def ptuples(f, vecx):
    polys = lagrange_basis(vecx)
    coords = lagrange_coords(f, vecx)
    stiple = np.linspace(-1,1,100)
    interstiple = np.array([interpol(coords,polys,t) for t in stiple])
    return np.vstack([stiple,interstiple])

for f in [f1,f2]:
    for n in [8, 16, 32]:
        linear = np.linspace(-1,1,n+1)
        chebyshev = chebyshev_transform(linear)
        p_linear = ptuples(f, linear)
        p_chebyshev = ptuples(f, chebyshev)
        plt.plot(np.linspace(-1,1),[f(t) for t in np.linspace(-1,1)])
        plt.plot(p_linear[0],p_linear[1])
        plt.plot(p_chebyshev[0],p_chebyshev[1])
        plt.ylim(-2,2)
        plt.title(f.__name__ + ' approximated by different $p_{%d}$' % n)
        plt.legend((f.__name__,'Linear-spaced $p_{%d}$' % n,'Chebyshev $p_{%d}$' % n))
        plt.show()


