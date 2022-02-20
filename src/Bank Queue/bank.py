from heapq import *

n, t = list(map(int, input().split()))
q = []
s = set()
for _ in range(48):
    q.append([])
    heappush(q[-1], (0, len(q)))
    s.add((0, len(q)))
choice = [None] * 48

for _ in range(n):
    ci, ti = list(map(int, input().split()))
    s.add((-ci, ti))
    for tt in range(ti + 1):
        heappush(q[tt], (-ci, ti))

ans = 0
for idx in range(t, -1, -1):
    while q[idx] and q[idx][0] not in s:
        heappop(q[idx])
    choice[idx] = heappop(q[idx])
    s.remove(choice[idx])
    ans -= choice[idx][0]

print(ans)