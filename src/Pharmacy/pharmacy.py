from collections import deque
from heapq import *
n, t = map(int, input().split())
pq, qr, qs, ct = [], [], [], 1e9
for _ in range(n):
    d, rs, k = input().split()
    d, k = map(int, (d, k))
    ct = min(ct, d)
    [qr, qs][rs=='S'].append((d, k))
qr, qs = deque(sorted(qr)), deque(sorted(qs))
ans = [[0, len(qs)], [0, len(qr)]]
while qr or qs:
    tmp, tmp2 = [], []
    while not tmp and qs and qs[0][0] <= ct: tmp.append(qs.popleft())
    while not tmp and not tmp2 and qr and qr[0][0] <= ct: tmp2.append(qr.popleft())
    if tmp: tup, wrs = tmp[0], 0
    else: tup, wrs = tmp2[0], 1
    dd, kk = tup
    if len(pq) < t:
        heappush(pq, (ct+kk, dd, wrs))
        ct = max(ct, min(qr[0][0] if qr else 1e10, qs[0][0] if qs else 1e10))
    else:
        [qs, qr][wrs].appendleft((dd, kk))
        ct = pq[0][0]
    while pq and pq[0][0] <= ct:
        tt, ss, wrs = heappop(pq)
        ans[wrs][0] += tt-ss
while pq:
    tt, ss, wrs = heappop(pq)
    ans[wrs][0] += tt-ss
(a, b), (c, d) = ans
print(a/b if b else 0, c/d if d else 0)