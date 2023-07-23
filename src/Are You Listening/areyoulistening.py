cx, cy, n = map(int, input().split())
circs = [[*map(int, input().split())] for _ in range(n)]
P = 100

def check(R):
    c = 0
    for x, y, r in circs: c += P**2*((x-cx)**2 + (y-cy)**2) <= (P*r+R)**2
    return c

lo, hi = 0, 10**9*P
while abs(lo-hi) > 1:
    mid = (lo+hi)//2
    if check(mid) > 2: hi = mid
    else: lo = mid
print(int(mid/P))