import sys; input = sys.stdin.readline
from collections import Counter
n, h = map(int, input().split())
ss = [int(input()) for _ in range(n)]
sd = Counter(ss[::2]); su = Counter(ss[1::2])
d, u = [n//2]*(h+2), [n//2]*(h+2)
for i in range(1, h+2): d[i] = d[i-1] - sd[i-1]
for i in range(h, -1, -1): u[i] = u[i+1] - su[h-i]
m = min(d[i]+u[i] for i in range(1, h+1))
print(m, sum(d[i]+u[i]==m for i in range(1, h+1)))