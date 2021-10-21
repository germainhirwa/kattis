n = int(input())
d = {}

import sys

for line in sys.stdin:
    d[line] = d.get(line, 0) + 1

for k in d:
    n = min(n, d[k])

ans = []
for k in d:
    if d[k] == n:
        ans.append(k)
ans.sort()
        
print("\n".join(ans))