import sys
f = c = 0
for l in sys.stdin:
    p, x, *y = l.split(); x = int(x)
    if p[-2] != 'i' and p[-1] != 'e': y = int(y[0])
    if p[0] == 'b': f += x; c += x*y
    elif p == 'sell': c *= (f-x)/f; f -= x
    elif p[1] == 'p': f *= x
    elif p[0] == 'm': n = f//x; c *= n*x/f if f else 1; f = n
    else: print(f*(x-max(0, 0.3*(x-c/f if f else 0))))