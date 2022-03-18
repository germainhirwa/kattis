c, s = input().split()
cs = {}
for l in c:
    if l not in cs:
        cs[l] = 0
    cs[l] += 1

i, j, ok = 0, 0, 1
while j < len(s) and i < len(c):
    if s[j] == c[i]:
        cs[c[i]] -= 1
        if cs[c[i]] == 0:
            del cs[c[i]]
        i += 1
    elif s[j] in cs:
        ok = 0
        break
    j += 1
print(['FAIL', 'PASS'][ok and i == len(c)])