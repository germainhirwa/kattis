import sys
from collections import Counter
v, e = map(int, input().split())
E, tour, w = Counter(), 0, 0
for l in sys.stdin:
    if e: 
        a, b = map(int, l.split())
        a -= 1; b -= 1; e -= 1
        E[(a, b)] += 1
    elif not w: w = int(l)
    elif not tour: tour = list(map(lambda x: int(x)-1, l.split()))
for i in range(w):
    a, b = tour[i], tour[i+1]
    if not E[(a, b)]: print(i+1), exit(0)
    E[(a, b)] -= 1
print(['too short', 'correct'][sum(E.values())==0])