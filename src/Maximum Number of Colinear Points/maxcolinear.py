import sys
input = sys.stdin.readline

def gcd(a, b):
    while b: a, b = b, a % b
    return a

while True:
    t = int(input())
    if t == 0: break
    h, v = {}, {}
    xy = [tuple(map(int, input().split())) for _ in range(t)]
    best = 1
    for i in range(t-1):
        x1, y1 = xy[i]
        h = {}
        for j in range(i+1, t):
            x2, y2 = xy[j]
            a, b = y2 - y1, x2 - x1
            d = gcd(a, b); a//=d; b//=d
            if b == 0 and a < 0: a, b = -a, -b
            tup = (a, b)
            if tup not in h: h[tup] = 1
            h[tup] += 1
        best = max(best, max(h.values(), default=1))
    print(best)