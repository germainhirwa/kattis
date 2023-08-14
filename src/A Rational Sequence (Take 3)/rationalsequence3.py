def f(n):
    p = q = 1
    for i in bin(n)[3:]:
        if int(i): p += q
        else: q += p
    return p, q

def g(p, q):
    s = []
    while p*q != 1:
        if p > q: p -= q; s.append('1')
        else: q -= p; s.append('0')
    s.append('1')
    return int(''.join(s[::-1]), 2)

import sys; input = sys.stdin.readline
for _ in range(int(input())):
    t, d = map(int, input().split())
    p, q = f(d)
    print(t, f'{p}/{q}')