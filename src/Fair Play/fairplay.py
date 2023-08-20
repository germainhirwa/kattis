from collections import Counter
import sys; input = sys.stdin.readline
n = int(input())
if n%2: print('impossible'), exit(0)
p = [tuple(map(int, input().split())) for _ in range(n)]; c = Counter(p)
a = 2*sum(i[0] for i in p)//n; b = 2*sum(i[1] for i in p)//n
for x, y in c:
    if c[(a-x, b-y)] != c[(x, y)]: print('impossible'), exit(0)
print('possible')