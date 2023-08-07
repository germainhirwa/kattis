import sys; input = sys.stdin.readline
from math import *
for _ in range(int(input())):
    CA = []
    for _ in range(int(input())):
        c, a = input().strip().split()
        CA.append((c, a))
    A = pi; X = Y = 0
    for c, a in CA:
        if c == 'fd': X += int(a)*cos(A); Y += int(a)*sin(A)
        elif c == 'bk': X -= int(a)*cos(A); Y -= int(a)*sin(A)
        elif c == 'lt': A += int(a)*pi/180
        else:           A -= int(a)*pi/180
    print(round(hypot(X, Y)))