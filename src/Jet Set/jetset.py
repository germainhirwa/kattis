longs = [2*int(input().split()[1])+360 for _ in range(int(input()))]
vis = [0]*720
for a, b in zip(longs, longs[1:]+[longs[0]]):
    if (b-a)%720 <= (a-b)%720:
        if b < a: b += 720
        for i in range(a, b+1): vis[i%720] = 1
    else:
        if a < b: a += 720
        for i in range(b, a+1): vis[i%720] = 1
for i in range(720):
    if not vis[i]: print('no', (i-360)/2), exit(0)
print('yes')