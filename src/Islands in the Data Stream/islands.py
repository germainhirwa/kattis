import sys

n = int(input())
for line in sys.stdin:
    arr = list(map(int, line.split()))
    c = arr[0]
    h = arr[1:]
    ss = sum(h)
    ans = 0
    while ss != 0:
        s, m = 0, -1
        for i in range(len(h)):
            if m == -1:
                if h[i] != 0:
                    s, m = i, h[i]
            elif h[i] == 0:
                for t in range(s, i):
                    ss -= m
                    h[t] -= m
                ans += 1
                m = -1
            else:
                m = min(m, h[i])
    print(c, ans)