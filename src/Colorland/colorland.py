import sys
from collections import deque

n = int(input())
cols = {}
arr = []
cnt = 0
for c in sys.stdin:
    c = c.strip()
    arr.append(c)
    if c not in cols:
        cols[c] = deque([])
    cols[c].append(cnt)
    cnt += 1

ans = 0
curr = -1
while cols:
    ans += 1
    col = max(cols, key=lambda x: cols[x][0])
    check = cols[col].popleft()
    if check == n - 1:
        print(ans)
        sys.exit(0)
    for col in list(cols.keys()):
        while cols[col] and cols[col][0] < check:
            cols[col].popleft()
        if not cols[col]:
            del cols[col]