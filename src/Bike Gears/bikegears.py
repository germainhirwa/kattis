from fractions import Fraction
input()
f = [*map(int, input().split())]
b = [*map(int, input().split())]
s = []
for i in f:
    for j in b: s.append((Fraction(i, j), i, j))
for _, f, b in sorted(s): print(f'({f},{b})')