import sys

def process(t):
    t = t.split()
    h, m = map(int, t[0].split(':'))
    return (h%12)*60 + m + 7200*(t[1] == 'p.m.')

n = -1
for l in sys.stdin:
    if n == -1: n, t = int(l), []
    else:
        n -= 1
        t.append(l.strip())
        if n == 0:
            n = -1
            for i in sorted(t, key=process): print(i)
            print()