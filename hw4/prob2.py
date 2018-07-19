import sympy as sym

x,y = sym.symbols('x y')
F = sym.Matrix([x**2 + y**2 - 4, x**2 - y**2 - 1])
print("F    =", F)

J = F.jacobian(sym.Matrix([x,y]))
print("J    =", J)

init = [(x,1),(y,1)]
vec0 = sym.Matrix([coord[1] for coord in init])
print("vec0 =", vec0)

h = J.subs(init).LUsolve(-F.subs(init))
print("h    =", h)

vec1 = h + vec0
print("vec1 =", vec1)
