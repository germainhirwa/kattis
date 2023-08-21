import sys; input = sys.stdin.readline
n, m = map(int, input().split())
p = [*map(int, input().split())]
t = [*map(int, input().split())]
h = [{} for _ in range(m)]
for i in range(n):
    j = min(range(m), key=lambda x: (abs(t[x]-p[i]), t[x]))
    d = abs(t[j]-p[i])
    if d not in h[j]: h[j][d] = []
    h[j][d].append(i)
tr = [0]*n
for i in range(m):
    if not h[i]: continue
    b = min(h[i])
    for j in h[i][b]:
        if not tr[j]: tr[j] = 1; break
print(sum(i==0 for i in tr))