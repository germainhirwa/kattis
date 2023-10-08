import sys; input()
h = dict(zip([*'IVXLCDM'], [1, 5, 10, 50, 100, 500, 1000]))
for l in sys.stdin:
    r = l.strip(); m = b = 0; d = []
    for i in r[::-1]: b = max(b, h[i]); d.append(b)
    d = d[::-1]
    for i in range(len(r)):
        if h[r[i]] < d[i]: m -= h[r[i]]
        else: m += h[r[i]]
    print(m)