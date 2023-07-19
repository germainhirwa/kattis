import sys; input = sys.stdin.readline
from math import ceil
n, a, b = int(input()), [*map(int, input().split())], [*map(int, input().split())]; z = [*zip(a, b)]
z = sorted([i for i in z if i[1] != -1], key=lambda x: x[1])
c = s = 0
for i in range(len(z)): s += z[i][0]; c = max(c, s/z[i][1])
print(ceil(c))