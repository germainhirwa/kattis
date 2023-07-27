import sys
from math import *
dp = [1]
for i in range(1_000_000): dp.append(dp[-1]+log10(i+1))
for i in sys.stdin: print(int(dp[int(i)]))