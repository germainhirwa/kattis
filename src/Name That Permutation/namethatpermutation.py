def kth(arr, idx):
    res = []
    pos = []
    n = len(arr)
    for i in range(n):
        pos.append(idx % (i + 1))
        idx = idx // (i + 1)
    for i in range(n):
        res.append(arr.pop(pos[-i-1]))
    return res

import sys

for line in sys.stdin:
    n, k = map(int, line.split())
    print(*kth(list(range(1, n + 1)), k))