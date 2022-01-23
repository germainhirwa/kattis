import sys

l, d, n = list(map(int, input().split()))
if l < 12:
    print(0)
else:
    ans = 0
    p = []
    for line in sys.stdin:
        p.append(int(line) - 5)
    p.sort()
    for i in range(1, len(p)):
        ans += (p[i] - p[i - 1]) // d - 1
    if not p:
        ans += (l - 12) // d + 1
    else:
        ans += (p[0] - 1) // d + (l - 10 - p[-1] - 1) // d
    print(ans)