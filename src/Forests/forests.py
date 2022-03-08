import sys

p, t = map(int, input().split())
h = [0] * p

for line in sys.stdin:
    pp, tt = map(int, line.split())
    h[pp - 1] += 2**tt

print(len(set(h)))