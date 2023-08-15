import sys; input = sys.stdin.readline
from math import *
for _ in range(int(input())):
    a, b, d = map(int, input().split())
    print(['No', 'Yes'][d % gcd(a, b) == 0])