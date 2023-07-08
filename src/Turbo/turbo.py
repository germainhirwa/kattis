class FenwickTree:
    def __init__(self, n):
        self.ft1 = [0]*(n+1)
        self.ft2 = [0]*(n+1)
        self.n = n
        self.add(1, n, 1)
    def add(self, l, r, v):
        p1, p2, p3, p4 = l, r+1, l, r+1
        while p1 <= self.n: self.ft1[p1] += v; p1 += (p1&(-p1))
        while p2 <= self.n: self.ft1[p2] -= v; p2 += (p2&(-p2))
        while p3 <= self.n: self.ft2[p3] += v*(l-1); p3 += (p3&(-p3))
        while p4 <= self.n: self.ft2[p4] -= v*r; p4 += (p4&(-p4))
    def get(self, r):
        s = 0; p1 = p2 = r
        while p1 > 0: s += r*self.ft1[p1]; p1 -= (p1&(-p1))
        while p2 > 0: s -= self.ft2[p2]; p2 -= (p2&(-p2))
        return s

import sys
n, a = int(sys.stdin.readline()), list(map(int, sys.stdin))
rv = {e:i for i, e in enumerate(a)}
ft, t = FenwickTree(n), 1
for i in range(n): c = rv[i//2+1 if t else n-i//2]+1; ft.add(c, c, -1); t, s = 1-t, ft.get(c-1); print(n-i-1-s if t else s)