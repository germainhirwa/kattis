class FenwickTree:
    def __init__(self, n):
        self.ft, self.n = [0]*(n+1), n
    def add(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx], idx = e+self.ft[idx], idx+(idx&(-idx))
    def get(self, idx):
        s, idx = 0, min(idx, self.n)
        while idx > 0: s, idx = s+self.ft[idx], idx-(idx&(-idx))
        return s

import sys
n, k = map(int, input().split())
ft = FenwickTree(n)
for line in sys.stdin:
    line = line.split()
    if line[0] == 'F':
        t = int(line[1])-1
        ft.add(t, 1-2*(ft.get(t+1)-ft.get(t)))
    else:
        l, r = map(int, line[1:])
        print(ft.get(r)-ft.get(l-1))