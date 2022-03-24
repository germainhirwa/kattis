import sys
from heapq import *

k, n = map(int, input().split())
y, p = map(int, input().split())
tribe = [(y, p)]

for line in sys.stdin:
    yy, pp = map(int, line.split())
    tribe.append((yy, pp))
tribe.sort(key=lambda x: x[0], reverse=True)

pq = list(map(lambda x: -x[1], tribe[-k:]))
heapify(pq)
tribe = tribe[:-k]

curr = 2011
while tribe:
    if pq[0] + p == 0:
        print(curr)
        sys.exit(0)
    heappop(pq)
    heappush(pq, -tribe.pop()[1])
    curr += 1
if pq[0] + p != 0:
    print('unknown')
else:
    print(curr)