import sys; input = sys.stdin.readline
from collections import deque
for _ in range(int(input())):
    m, S = map(int, input().split()); S **= 2
    coins = [[*map(int, input().split())] for _ in range(m)]; input()
    q = deque([(0, 0)]); seen = {0}; ans = -1
    while q and ans == -1:
        d, xy = q.popleft()
        x, y = xy//S, xy%S
        for dx, dy in coins:
            p = (x+dx)**2 + (y+dy)**2
            if p == S: ans = d+1; break
            if p > S: continue
            if (s:=(x+dx)*S+y+dy) in seen: continue
            seen.add(s), q.append((d+1, s))
    print('not possible' if ans == -1 else ans)