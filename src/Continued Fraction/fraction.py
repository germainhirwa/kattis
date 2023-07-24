from fractions import Fraction
a, b = map(int, input().split())
f1, f2 = [*map(int, input().split())], [*map(int, input().split())]

def tof(cf):
    s = Fraction(cf[-1])
    for i in range(len(cf)-2, -1, -1): s = cf[i] + Fraction(1, s)
    return s

def toc(f):
    s = []
    while True:
        s.append(int(f)); f -= int(f)
        if f == 0: return s
        f = Fraction(1, f)

r1, r2 = tof(f1), tof(f2)
print(*toc(r1+r2)), print(*toc(r1-r2)), print(*toc(r1*r2)), print(*toc(r1/r2))