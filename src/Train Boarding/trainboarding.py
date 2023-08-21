n, l, p = map(int, input().split())
x = [int(input()) for _ in range(p)]
d = [(i*l+l//2) for i in range(n)]
q = 0; h = {}
for i in x:
    b = min(d, key=lambda j: (abs(i-j), -j))
    q = max(q, abs(i-b))
    if b not in h: h[b] = 0
    h[b] += 1
print(q), print(max(h.values()))