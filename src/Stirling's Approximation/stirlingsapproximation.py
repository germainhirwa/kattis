import sys
from math import exp, pi, log

e = exp(1)
for line in sys.stdin:
    n = int(line)
    if n != 0:
        epn = log(e/n)
        r = log(1e14)+1 if n != 1 else log(1e14)
        for i in range(2, n): r += log(i) + epn
        r += epn - log(2*pi*n)/2
        r = str(exp(r)).replace('.', '')
        print(f'{r[0]}.{r[1:]}')