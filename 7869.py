import math
import sympy

x1, y1, r1, x2, y2, r2 = map(float, input().split())
x, y = sympy.symbols('x y')

f1 = sympy.Eq((x - x1) ** 2 + (y - y1) ** 2, r1 ** 2)
f2 = sympy.Eq((x - x2) ** 2 + (y - y2) ** 2, r2 ** 2)
m1, m2 = sympy.solve([f1, f2], (x, y))

t1 = sympy.symbols('t1')
sc1 = ((m1[y] - y1) / math.sqrt((m1[x] - x1) ** 2 + (m1[y] - y1) ** 2)) * (
        (m1[x] - x1) / math.sqrt((m1[x] - x1) ** 2 + (m1[y] - y1) ** 2))
cs1 = ((m1[x] - x2) / math.sqrt((m1[x] - x2) ** 2 + (m1[y] - y2) ** 2)) * (
            (m1[y] - y2) / math.sqrt((m1[x] - x2) ** 2 + (m1[y] - y2) ** 2))
k1 = sympy.Eq(sc1 - cs1,  sympy.sin(t1))
print(sympy.solve(k1))

t2 = sympy.symbols('t2')
sc2 = ((m2[y] - y1) / math.sqrt((m2[x] - x1) ** 2 + (m2[y] - y1) ** 2)) * (
        (m2[x] - x1) / math.sqrt((m2[x] - x1) ** 2 + (m2[y] - y1) ** 2))
cs2 = ((m2[x] - x2) / math.sqrt((m2[x] - x2) ** 2 + (m2[y] - y2) ** 2)) * (
            (m2[y] - y2) / math.sqrt((m2[x] - x2) ** 2 + (m2[y] - y2) ** 2))
k2 = sympy.Eq(sc2 - cs2,  sympy.sin(t2))
print(sympy.solve(k2))