h = [*map(int, input().split())][1:]
b = [*map(int, input().split())][1:]
s = max(sum(h), sum(b))
dph = [[float('inf')]*(s+1) for _ in range(len(h)+1)]
dpb = [[float('inf')]*(s+1) for _ in range(len(b)+1)]
dph[0][0] = dpb[0][0] = 0
for i in range(1, len(h)+1):
    for j in range(s+1):
        if j>=h[i-1]: dph[i][j] = min(dph[i-1][j], dph[i-1][j-h[i-1]]+1)
        else: dph[i][j] = dph[i-1][j]
for i in range(1, len(b)+1):
    for j in range(s+1):
        if j>=b[i-1]: dpb[i][j] = min(dpb[i-1][j], dpb[i-1][j-b[i-1]]+1)
        else: dpb[i][j] = dpb[i-1][j]
best = 1e9
for a, b in zip(dph[-1], dpb[-1]):
    if float('inf')!=a+b>0: best = min(best, a+b)
print(best if best != 1e9 else 'impossible')