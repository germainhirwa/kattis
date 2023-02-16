class FenwickTree:
    def __init__(self, n):
        self.ft, self.n = [0]*(n+1), n
    def add(self, idx, e):
        while idx <= self.n: self.ft[idx], idx = e+self.ft[idx], idx+(idx&(-idx))
    def get(self, idx):
        s = 0
        while idx > 0: s, idx = s+self.ft[idx], idx-(idx&(-idx))
        return s

import sys
n, q = map(int, input().split())
v = list(map(int, input().split()))
p = list(map(int, input().strip()))
ft = [None] + [FenwickTree(n) for _ in range(6)]
for i in range(n): ft[p[i]].add(i+1, 1)
for line in sys.stdin:
    t, kpl, pvr = map(int, line.split())
    if t == 1:
        # replace p[kpl-1] with pvr
        ft[p[kpl-1]].add(kpl, -1), ft[pvr].add(kpl, 1)
        p[kpl-1] = pvr
    elif t == 2:
        # replace v[kpl-1] with pvr
        v[kpl-1] = pvr
    else:
        # get [kpl, pvr] sum from all FTs
        print(sum(v[i-1]*(t.get(pvr)-t.get(kpl-1)) for i, t in enumerate(ft) if t != None))