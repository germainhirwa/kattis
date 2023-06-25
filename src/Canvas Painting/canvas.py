from heapq import *
for _ in range(int(input())):
    n, q, s = int(input()), list(map(int, input().split())), 0
    heapify(q)
    while len(q) > 1:
        a, b = heappop(q), heappop(q)
        s += a + b
        heappush(q, a + b)
    print(s)