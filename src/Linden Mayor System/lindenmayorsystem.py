n, m = map(int, input().split())
c = dict(input().split(' -> ') for _ in range(n))
s = [*input()]
for _ in range(m):
    s2 = s.copy()
    for i in range(len(s2)): s2[i] = c[s2[i]] if s2[i] in c else s2[i]
    s = [*''.join(s2)]
print(''.join(s))