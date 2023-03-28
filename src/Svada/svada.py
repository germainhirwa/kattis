T, AB, CD = int(input()), [], []
for _ in range(int(input())):
    a, b = map(int, input().split())
    AB.append((a, b))
for _ in range(int(input())):
    c, d = map(int, input().split())
    CD.append((c, d))
lo, hi = 0, T
while abs(lo - hi) > 2:
    t, k = (lo + hi)//2, 0
    t2 = T-t
    for a, b in AB: k += max((t-a)//b + (t>=a), 0)
    for c, d in CD: k -= max((t2-c)//d + (t2>=c), 0)
    if k == 0: break
    elif k > 0: hi = t
    else: lo = t+1
if k == 0: lo = hi = t
min_d, best, lo, hi = 1e9, None, lo-1, hi+1
for t in range(2*lo, 2*hi):
    t /= 2
    k, t2 = 0, T-t
    for a, b in AB: k += max((t-a)//b + (t>=a), 0)
    for c, d in CD: k -= max((t2-c)//d + (t2>=c), 0)
    if abs(k) < min_d: min_d, best = abs(k), t
print(int(best))