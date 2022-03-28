def e(n, m, p):
    if n == 0:
        return m
    if 2*m*p < 1:
        return e(n - 1, (m + 0.25/m - p)/(1 - p), p)
    return e(n - 1, m*(p + 1), p)

import sys
for line in sys.stdin:
    n, p = map(float, line.split())
    if n:
        print('%.3f'%(e(int(n), 1, p)))