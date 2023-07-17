n, k = map(int, input().split())
a = [*map(int, input().split())]
t = a.pop(k)
if t > 300: print(0, 0), exit(0)
ac, p, c = 1, t, t
for i in sorted(a):
    if c+i > 300: break
    c += i; p += c; ac += 1
print(ac, p)