k, n = map(int, input().split())
arr = []

import sys
for line in sys.stdin:
    arr.append(list(map(int, line.split())))

arr.sort(key=lambda x: x[1])
ans = 0
hi = -1
for a, b in arr:
    if hi <= a:
        hi = b
        ans += 1
print(['NO', 'YES'][int(ans >= k)])