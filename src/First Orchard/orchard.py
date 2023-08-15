r, g, b, y, s = map(int, input().split())

m = {}
def p(r, g, b, y, s):
    if s == 0: return 0
    if r == g == b == y == 0: return 1
    k = 10000*r+1000*g+100*b+10*y+s
    if k in m: return m[k]
    a = 1/6*p(r, g, b, y, s-1)
    if max(r, g, b, y) == r:    a += 1/6*p(r-1, g, b, y, s)
    elif max(r, g, b, y) == g:  a += 1/6*p(r, g-1, b, y, s)
    elif max(r, g, b, y) == b:  a += 1/6*p(r, g, b-1, y, s)
    else:                       a += 1/6*p(r, g, b, y-1, s)
    c = 1
    if r: a += 1/6*p(r-1, g, b, y, s)
    else: c -= 1/6
    if g: a += 1/6*p(r, g-1, b, y, s)
    else: c -= 1/6
    if b: a += 1/6*p(r, g, b-1, y, s)
    else: c -= 1/6
    if y: a += 1/6*p(r, g, b, y-1, s)
    else: c -= 1/6
    m[k] = a/c; return m[k]

print(p(r, g, b, y, s))