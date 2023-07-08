class FenwickTree:
    def __init__(self, n, r):
        self.ft1 = [0]*(n+r+1)
        self.ft2 = [0]*(n+r+1)
        self.n = n+r
        self.add(0, n, 1)
    def add(self, l, r, v): # arr[l:r] += v
        l += 1
        p1, p2, p3, p4 = l, r+1, l, r+1
        while p1 <= self.n: self.ft1[p1] += v; p1 += (p1&(-p1))
        while p2 <= self.n: self.ft1[p2] -= v; p2 += (p2&(-p2))
        while p3 <= self.n: self.ft2[p3] += v*(l-1); p3 += (p3&(-p3))
        while p4 <= self.n: self.ft2[p4] -= v*r; p4 += (p4&(-p4))
    def get(self, r): # sum(arr[:r])
        s = 0; p1 = p2 = r
        while p1 > 0: s += r*self.ft1[p1]; p1 -= (p1&(-p1))
        while p2 > 0: s -= self.ft2[p2]; p2 -= (p2&(-p2))
        return s

import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n, r = map(int, input().split()); a = [*range(r)]
    m, ft = n-1, FenwickTree(n, r)
    pos = [*range(n, 0, -1)]
    for i in map(int, input().split()):
        n += 1
        ft.add(pos[i-1]-1, pos[i-1], -1)
        print(m-ft.get(pos[i-1]), end=' ')
        pos[i-1] = n; ft.add(n-1, n, 1)
    print()