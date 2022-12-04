n = int(input())
pts = {}
for i in range(n):
    m = input()
    for j in range(n):
        if m[j].isupper():
            pts[m[j]] = (i, j)

ans = 0
for a in pts:
    for b in pts:
        for c in pts:
            (xa, ya), (xb, yb), (xc, yc) = pts[a], pts[b], pts[c]
            ans += len({a, b, c}) == 3 and (xb - xa) * (yc - ya) == (xc - xa) * (yb - ya)
print(ans // 6)