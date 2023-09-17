from collections import *
n = int(input()); s = input()
print(max([sum(c.values()) for c in [Counter(s[i:j+1]) for i in range(n) for j in range(i, n)] if len({*c.values()}) == 1], default=0))