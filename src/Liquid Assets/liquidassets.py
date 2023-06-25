import string
n, w = int(input()), input().strip().split()
for i in range(n):
    s, r, r2 = w[i], '', ''
    for l in string.ascii_lowercase:
        while True:
            s2 = s.replace(l*2, l)
            if s2 == s: break
            s = s2
    if s and s[0] in 'aeiou': r, s = s[0], s[1:]
    if s and s[-1] in 'aeiou': r2, s = s[-1], s[:-1]
    for v in 'aeiou': s = s.replace(v, '')
    w[i] = r+s+r2
print(' '.join(w))