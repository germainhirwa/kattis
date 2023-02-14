class FenwickTree:
    def __init__(self, n):
        self.ft = [0]*(n+1)
        self.n = n
    def add(self, idx, e):
        idx += 1
        while idx <= self.n:
            self.ft[idx] += e
            idx += idx & (-idx)
    def get(self, idx):
        s = 0
        while idx > 0:
            s += self.ft[idx]
            idx -= idx & (-idx)
        return s

import sys
n, q = map(int, input().split())
ft = FenwickTree(n)
for line in sys.stdin:
    line = line.split()
    if line[0] == '+':
        a, b = map(int, line[1:])
        ft.add(a, b)
    else:
        print(ft.get(int(line[1])))