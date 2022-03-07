from heapq import *

h, c = map(int, input().split())
pq = []
for _ in range(c):
    a, d = map(int, input().split())
    pq.append((a + d, d))
heapify(pq)

for _ in range(h):
    apd, d = heappop(pq)
    heappush(pq, (apd + d, d))

adm = max(pq, key=lambda x: x[0] - x[1])
print(adm[0] - adm[1])