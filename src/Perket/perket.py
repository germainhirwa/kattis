def ps(n):
    s = [[]]
    for i in n:
        s2 = []
        for j in s: s2.append(j), s2.append(j+[i])
        s = s2
    return s[1:]

d = 1e9
for i in ps([[*map(int, input().split())] for _ in range(int(input()))]):
    s, b = 1, 0
    for ss, bb in i: s *= ss; b += bb
    d = min(d, abs(s-b))
print(d)