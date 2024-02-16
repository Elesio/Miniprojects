from sympy import *
import math
x = Symbol('x')
pi = math.pi * -1
Rv = 263483213.06276882 
Rh = 301472741.1624469
print(solve(x**2 - 1, x))
print(solve(exp(pi * Rv / x) + exp(pi * Rh / x) - 1, x))
#print(solve(math.exp(pi * Rv / x) + math.exp(pi * Rh / x) - 1, x))