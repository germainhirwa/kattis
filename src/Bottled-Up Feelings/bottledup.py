s, v1, v2 = map(int, input().split())
best = (1e9, 1e9)
for i in range(s//v1+1):
    v = s-v1*i
    for j in range(v//v2-1, v//v2+2):
        if i*v1+j*v2 == s: best = min(best, (i, j), key=sum)
if best[0] == 1e9: print('Impossible')
else: print(*best)