from fractions import Fraction
for _ in range(int(input())):
    t, d, f = map(float, input().split())
    print(int(t), Fraction(f).limit_denominator(int(d)))