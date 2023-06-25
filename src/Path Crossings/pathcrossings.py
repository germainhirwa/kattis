p, n = map(int, input().split())
pings = []
for _ in range(n):
    k, x, y, t = map(int, input().split())
    pings.append((t, k, x, y))
pings.sort()
cross = set()
for i in range(len(pings)):
    t, k, x, y = pings[i]
    l, r = i-1, i+1
    while l >= 0 and pings[l][0] > t-11:
        t2, k2, x2, y2 = pings[l]
        if k != k2 and (x-x2)**2 + (y-y2)**2 <= 1e6: cross.add((min(k, k2), max(k, k2)))
        l -= 1
    while r < len(pings) and pings[r][0] < t+11:
        t2, k2, x2, y2 = pings[r]
        if k != k2 and (x-x2)**2 + (y-y2)**2 <= 1e6: cross.add((min(k, k2), max(k, k2)))
        r += 1
print(len(cross))
for i in sorted(cross): print(*i)