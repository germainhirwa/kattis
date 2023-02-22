import sys
input()
for l in sys.stdin:
    l = int(l)
    b, p, s, e = 0, 2**l, 10**(l-1), 10**l
    while not s <= p < e:
        b += 1
        p = 11*p//2
    print(*([11]*b+[2]*(l-b)))