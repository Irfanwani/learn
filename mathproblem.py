from sympy import Symbol, solve, Eq

from matplotlib import pyplot


b = Symbol('b')

mu = 4

v = [i for i in range(1, 11)]

A  = 2 + 2*(mu**6) - 4*(mu**3)


B = [4*(mu**3 * v[i]) - 2*v[i] - 2*(mu**6 *v[i]) - 8 - 4*(mu**6) + 12*(mu**3) for i in range(len(v))]

C = [5*v[i] + mu**6 * v[i] - 4*(mu**3 * v[i]) + mu**6 - 10*(mu**3) + 11 for i in range(len(v))]

D = [2*(mu**3) - 4*v[i] - 6 for i in range(len(v))]

E = [v[i] + 1 for i in range(len(v))]

eq = [A*(b**4) + (b**3)*B[i] + (b**2)*C[i] + (b)*D[i] + E[i] for i in range(len(v))]

eqs = [Eq(i, 0) for i in eq]


# print(eqs)

vls = []

for i in eqs:
    vls.append(solve(i))


# print(vls)

finalres = [i[0] for i in vls]
print(finalres)
pyplot.plot(v, finalres)

pyplot.show()