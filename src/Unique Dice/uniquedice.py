import sys

def orient(a, b, c, d, e, f):
    # flip + swap == 2
    p = [
        (a, b, c, d, e, f),
        (a, b, e, f, d, c),
        (a, b, d, c, f, e),
        (a, b, f, e, c, d),
        (b, a, d, c, e, f),
        (b, a, c, d, f, e),
        (b, a, e, f, c, d),
        (b, a, f, e, d, c),
    ]
    return min(map(min, [p, map(lambda x: x[2:] + x[:2], p), map(lambda x: x[-2:] + x[:-2], p)]))

n = int(input())
m = {}
for line in sys.stdin:
    a, b, c, d, e, f = map(int, line.split())
    res = orient(a, b, c, d, e, f)
    if res not in m:
        m[res] = 0
    m[res] += 1
print(max(m.values()))