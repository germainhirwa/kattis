import sys; input = sys.stdin.readline
n = int(input()); a = [*map(lambda x: int(x)-1, input().split())]; r = 0; d = [0]*n
for i in range(n):
    if d[i]: continue
    d[i] = 1
    if a[i] == i: continue
    p = a[i]
    while p != i: r += 1; d[p] = 1; p = a[p]
    r += 2
print(r)