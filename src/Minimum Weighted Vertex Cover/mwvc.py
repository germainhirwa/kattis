import sys; input = sys.stdin.readline
import time

T = time.time() + 1.94
v, e = map(int, input().split())
w = [*map(int, input().split())]
al = [[] for _ in range(v)]
for _ in range(e): a, b = map(int, input().split()); al[a].append(b), al[b].append(a)
elw = {(a, b):1 for a in range(v) for b in al[a] if a < b}

# Bar-Yehuda and Even algorithm
def bye(w):
    w2 = w.copy()
    for a, b in elw:
        m = min(w2[a], w2[b])
        w2[a] -= m; w2[b] -= m
    return {i for i in range(v) if w2[i] == 0}

# Naive algorithm
def naive(w):
    u = [0]*v
    for a, b in elw:
        if w[a] < w[b]: u[a] = 1
        elif w[b] < w[a]: u[b] = 1
        else: u[a] = 1 # guaranteed a < b
    return {i for i in range(v) if u[i]}

def kt(val, nve, opt):
    if nve == opt: return int(val == opt)
    return 0.02**((val-opt)/(nve-opt))

def weight(c):
    s = 0
    for i in c: s += w[i]
    return s

rv = {*range(v)}
def score(c, inc):
    mi, mii, ma, maa = 1e10, 5000, 0, 0
    cc = [*c] if inc else rv-c
    for u in cc:
        if time.time() > T: kill()
        c1 = 0
        if inc:
            c.discard(u)
            for x in al[u]:
                if x not in c:
                    if (u, x) in elw: c1 += elw[(u, x)]
                    else: c1 += elw[(x, u)]
            c.add(u)
            cmp = c1/w[u]
            if cmp < mi: mi, mii = cmp, u
        else:
            for x in al[u]:
                if x not in c:
                    if (u, x) in elw: c1 += elw[(u, x)]
                    else: c1 += elw[(x, u)]
            cmp = c1/w[u]
            if cmp > ma: ma, maa = cmp, u
    return mii if inc else maa

def kill():
    print(wp, *cp), exit(0)

c = bye(w)
cp, wp = c.copy(), weight(c)

# Local search
# https://drops.dagstuhl.de/opus/volltexte/2022/16546/pdf/LIPIcs-SEA-2022-12.pdf
uncov = set()
while True:
    u = score(c, 1)
    c.discard(u) # Remove vertex u with lowest score(u) from C
    for i in al[u]:
        if i not in c:
            if u < i: uncov.add((u, i))
            else: uncov.add((i, u))
    while uncov: # while C is not a vertex cover
        vv = score(c, 0)
        c.add(vv) # Add vertex v with highest score(v) to C
        for a, b in [*uncov]:
            if a == vv or b == vv: uncov.discard((a, b))
        for a, b in uncov: # Add 1 to the weight of each uncovered edge
            elw[(a, b)] += 1
    ww = weight(c)
    if wp > ww: cp, wp = c.copy(), ww