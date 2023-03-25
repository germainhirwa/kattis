l, m = map(int, input().split())
f = []
for _ in range(m):
    n, p, c, t, r = input().split(',')
    p, c, t, r = map(int, [p, c, t, r])
    s = 10080*c*t/(t+r)
    if s >= l: f.append((n, p))
if not f: print('no such mower')
else:
    q = min([x[1] for x in f])
    f = [x[0] for x in f if x[1] == q]
    for i in f: print(i)