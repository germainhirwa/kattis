from heapq import *
n, m = map(int, input().split()); s = [(0, 0) for _ in range(m)]; b = 0
for i in sorted(map(int, input().split()), reverse=True):
    while True:
        c, t = heappop(s)
        if t == 2: b = max(b, c)
        else: break
    heappush(s, (c+i, t+1))
print(max(max(s)[0], b))