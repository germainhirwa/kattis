s = input(); a = []; b = []; n = len(s)
for i in s:
    if i == 'B': a.append(1), b.append(-1)
    else: a.append(-1), b.append(1)
lm = [(a[0], 0, -1)]*n
for i in range(1, n): lm[i] = max((a[i], -i, -i-1), (lm[i-1][0] + a[i], lm[i-1][1], -i-1))
s1 = max(lm)
lm = [(b[0], 0, -1)]*n
for i in range(1, n): lm[i] = max((b[i], -i, -i-1), (lm[i-1][0] + b[i], lm[i-1][1], -i-1))
s2 = max(lm)
r, a, b = max(s1, s2)
print(-a+1, -b)