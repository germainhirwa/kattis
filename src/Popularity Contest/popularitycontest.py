n, m = list(map(int, input().split()))
coeff = [-i-1 for i in range(n)]
import sys

for line in sys.stdin:
    a, b = list(map(int, line.split()))
    coeff[a - 1] += 1
    coeff[b - 1] += 1
print(' '.join(list(map(str, coeff))))