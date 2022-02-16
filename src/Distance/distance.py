import sys

n = int(input())
s, a = [], []
for line in sys.stdin:
    x, y = list(map(int, line.split()))
    s.append(x)
    a.append(y)

ans = 0
for arr in s, a:
    arr.sort()
    for i in range(n):
        ans += (2*i - n + 1) * arr[i]
print(ans)