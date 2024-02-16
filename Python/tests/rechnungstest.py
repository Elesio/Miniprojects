import math
a = 1.2783e+09
Rv = 263483213.06276882
Rh = 301472741.1624469

pi = math.pi * -1
b = math.exp(pi * Rv / a)
c = math.exp(pi * Rh / a) - 1
d = c + b
e = math.exp(pi * Rv / a) + math.exp(pi * Rh / a) - 1
print(e)