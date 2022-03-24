import sys
from heapq import *

n, k = map(int, input().split())
pq, leave = [], set()
for line in sys.stdin:
    q = line.split()
    if q[0] == '1':
        heappush(pq, (k*int(q[1]) - int(q[3]), q[2]))
    elif q[0] == '2':
        while pq and pq[0][1] in leave:
            heappop(pq)
        if not pq:
            print('doctor takes a break')
        else:
            print(heappop(pq)[1])
    else:
        leave.add(q[2].strip())