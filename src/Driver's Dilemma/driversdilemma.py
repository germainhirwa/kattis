c, x, m = list(map(float, input().split(" ")))

ms = 0
for _ in range(6):
    s, f = list(map(float, input().split(" ")))
    s = int(s)
    if (s/f + x)*(m/s) <= c/2:
        ms = max(ms, s)

if ms == 0:
    print("NO")
else:
    print("YES", ms)