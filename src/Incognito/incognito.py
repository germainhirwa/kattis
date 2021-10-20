n = int(input())
for _ in range(n):
    k = int(input())
    d = {}
    for _ in range(k):
        a, c = input().strip().split()
        d[c] = d.get(c, []) + [a]
    ans = 1
    for t in d:
        ans *= len(set(d[t])) + 1
    print(ans - 1)