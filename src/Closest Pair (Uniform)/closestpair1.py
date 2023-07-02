import sys

def cpp(px, py):
    if len(px) < 40: # just brute-force it
        d, pair = 1e9, None
        for i in range(len(px)-1):
            for j in range(i+1, len(px)):
                if (d2:=abs(px[i] -px[j])) < d: d, pair = d2, (px[i], px[j])
        return d, pair
    mid = len(px)//2
    xmid = px[mid].real
    py1, py2 = [], []
    for i in py:
        if i.real < xmid: py1.append(i)
        else: py2.append(i)
    d1, pair1 = cpp(px[:mid], py1)
    d2, pair2 = cpp(px[mid:], py2)
    if d1 < d2: d, pair = d1, pair1
    else:       d, pair = d2, pair2
    q = [i for i in py if abs(i.real - xmid) < d]
    for i in range(len(q)-1):
        for j in range(i+1, min(i+2, len(q))):
            if (d2:=abs(q[i] - q[j])) < d: d, pair = d2, (q[i], q[j])
            else: break
    return d, pair

n = -1
gr, gi = lambda c: c.real, lambda c: c.imag
for l in sys.stdin:
    if n == -1: n, p = int(l), []
    else:
        x, y = map(float, l.split())
        p.append(complex(x, y))
        n -= 1
        if n == 0:
            px, py = sorted(p, key=gr), sorted(p, key=gi)
            _, (p1, p2) = cpp(px, py)
            print(p1.real, p1.imag, p2.real, p2.imag)
            n = -1