import sys; input = sys.stdin.readline
n = int(input()); lr = input().strip()
s = []; c = lr[0]; t = 1
for i in range(1, n-1):
    if lr[i] == c: t += 1
    else: s.append((c, t)); c = lr[i]; t = 1
s.append((c, t))
pos = 0; v = [*range(1, n+1)]
for d, a in s:
    if d == 'L': v[pos:pos+a+1] = v[pos:pos+a+1][::-1]
    pos += a
for i in v: print(i)