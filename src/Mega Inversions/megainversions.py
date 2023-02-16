n, arr = int(input()), list(map(lambda x: int(x)-1, input().split()))

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
        s, idx = 0, min(idx, self.n)
        while idx > 0:
            s, idx = s+self.ft[idx], idx-(idx&(-idx))
        return s

f, g = FenwickTree(n), FenwickTree(n)
for i in range(n):
    f.add(i, g.get(n) - g.get(arr[i]+1))
    g.add(arr[i], 1)
s, g = 0, FenwickTree(n)
for i in range(n):
    s += g.get(n) - g.get(arr[i]+1)
    g.add(arr[i], f.get(i+1) - f.get(i))
print(s)