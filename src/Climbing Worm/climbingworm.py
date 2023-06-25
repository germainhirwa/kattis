a, b, h = map(int, input().split())
p, t, s = 0, 0, 1
d = [-b, a]
while p < h:
    t += 0 if s==b==0 else s
    p += d[s]
    s = 1-s
print(t)