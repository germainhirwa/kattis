def lis(arr):
    def upper_bound(sub, idx):
        lo, hi = 0, len(sub) - 1
        while hi > lo:
            mid = (lo + hi) // 2
            if arr[sub[mid]] < arr[idx]: lo = mid + 1
            else: hi = mid
        return hi
    temp = []
    par = [None] * len(arr)
    for i in range(len(arr)):
        if not temp or arr[i] > arr[temp[-1]]:
            if temp: par[i] = temp[-1]
            temp.append(i)
        else:
            rep = upper_bound(temp, i)
            temp[rep] = i
            if rep != 0: par[i] = temp[rep - 1]
    if not temp: return 0
    ans = 0
    curr = temp[-1]
    while curr != None:
        ans += 1
        curr = par[curr]
    return ans

import sys; input = sys.stdin.readline
n = int(input())
xh, yh, xw, yw = map(int, input().split())
if xh > xw: xh, xw, yh, yw = xw, xh, yw, yh
if yh <= yw: ee = sorted([*map(int, input().split())] for _ in range(n))
else: ee = [(x, -y) for x, y in sorted(([*map(int, input().split())] for _ in range(n)), key=lambda x: (x[0], -x[1]))]; yh, yw = -yh, -yw
ee = [(x, y) for x, y in ee if xh <= x <= xw and min(yh, yw) <= y <= max(yh, yw)]
print(lis([len(ee)*e+i for i, e in enumerate([p[1] for p in ee])]))