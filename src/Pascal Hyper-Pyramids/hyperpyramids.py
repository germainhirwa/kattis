from math import *
D, H = map(int, input().split())
can = set()
def bt(v, m, idx, h):
    if idx == D-1: return can.add(v//factorial(h))
    if (D-idx)*m > h: return
    for k in range(m, h//(D-idx)+1): bt(v//factorial(k), k, idx+1, h-k)
bt(factorial(H-1), 0, 0, H-1)
for i in sorted(can): print(i)