from fractions import Fraction
import sys; input = sys.stdin.readline
N, Q = map(int, input().split())
C = [[*map(int, input().split())] for _ in range(N)]
for _ in range(Q):
    a, b, t = map(int, input().split())
    (s1, e1), (s2, e2) = C[a-1], C[b-1]
    f = Fraction(e2-s2, e1-s1)*(t-s1)+s2
    print(f'{f.numerator}/{f.denominator}')