from collections import Counter
from math import log10
n, c = int(input()), list(map(int, input().split()))
s, f = sum(c), list(Counter(c).values())
print(sum(map(log10, range(1, s+1))) - s*log10(365) + sum(map(log10, [365-i for i in range(n)])) - sum([sum(map(log10, range(1, i+1))) for i in f+c]))