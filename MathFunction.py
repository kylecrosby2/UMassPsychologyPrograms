import math
import sympy
from sympy import *
x, y, z, t = symbols('x y z t')
a, b, c, d = symbols('a b c d', real=True)
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
init_printing()
eqn = Eq(1+a**2+b**2+c**2+d**2, 5)
print(solveset(eqn, a))
