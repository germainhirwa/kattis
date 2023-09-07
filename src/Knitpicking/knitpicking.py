import sys; input = sys.stdin.readline
n = int(input()); h = {}; ok = 0
for _ in range(n):
    i, j, k = input().split(); k = int(k)
    if i not in h: h[i] = {x:0 for x in 'LRA'}
    h[i][j[0].upper()] += k
for u in h:
    if h[u]['A'] > 1 or (h[u]['A'] and (h[u]['L']+h[u]['R'])) or h[u]['L']*h[u]['R']: ok = 1; break
print(sum(max(h[u]['L'], h[u]['R'], 1) for u in h)+1 if ok else 'impossible')