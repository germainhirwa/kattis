from collections import defaultdict
from heapq import *
import sys

n = None
for line in sys.stdin:
    if n == None:
        n, k = map(int, line.split())
    else:
        arr = map(int, line.split())
freq = defaultdict(lambda: 0)

for i in arr:
    freq[i] -= 1

pq = list(freq.values())
heapify(pq)

for _ in range(k):
    heappush(pq, heappop(pq) + 1)
print(-pq[0])