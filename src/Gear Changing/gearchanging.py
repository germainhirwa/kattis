n, m, p = map(int, input().split())
c, d = [list(map(int, input().split())) for _ in range(2)]
r = sorted(ci/di for ci in c for di in d)
print(['Time to change gears!', 'Ride on!'][max([b/a-1 for a, b in zip(r, r[1:])], default=0) <= p/100])