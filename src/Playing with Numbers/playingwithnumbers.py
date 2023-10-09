import sys; input = sys.stdin.readline
n = int(input()); p = [[*map(int, input().split())] for _ in range(n)]

'''
Input:
8
585 994
89 563
140 411
890 120
723 664
603 367
936 412
842 520

Output:
936 994 936 994
936 994 140 411
936 994 89 120
936 994 89 120
936 994 89 120
936 994 89 120
585 994 89 120
89 120 89 120

Observation:
The first n-2 maximums are the same, the last n-2 minimums are the same!
'''

from math import *
result = [[(0, 0), (1000, 1000)] for _ in range(n)]
mi2p, mi2s, mi3p, mi3s = [[1000]*(n+1) for _ in range(4)]
ma2p, ma2s, ma3p, ma3s = [[0]*(n+1) for _ in range(4)]
for i in range(n):
    mi2p[i+1] = min(mi2p[i], p[i][0]); mi3p[i+1] = min(mi3p[i], p[i][1])
    ma2p[i+1] = max(ma2p[i], p[i][0]); ma3p[i+1] = max(ma3p[i], p[i][1])
    mi2s[n-i-1] = min(mi2s[n-i], p[n-i-1][0]); mi3s[n-i-1] = min(mi3s[n-i], p[n-i-1][1])
    ma2s[n-i-1] = max(ma2s[n-i], p[n-i-1][0]); ma3s[n-i-1] = max(ma3s[n-i], p[n-i-1][1])
result[0] = [(ma2p[-1], ma3p[-1]) for _ in '..']; result[-1] = [(mi2p[-1], mi3p[-1]) for _ in '..']
for i in range(n-2): result[i][0] = result[0][0]; result[-i-1][1] = result[-1][1]
if n > 1:
    # what's left: result[1][1] and result[-2][0]
    for i in range(n):
        result[1][1] = min(result[1][1], (min(p[i][0], max(ma2p[i], ma2s[i+1])), min(p[i][1], max(ma3p[i], ma3s[i+1]))), key=lambda x: x[0]*log(2)+x[1]*log(3))
        result[-2][0] = max(result[-2][0], (max(p[i][0], min(mi2p[i], mi2s[i+1])), max(p[i][1], min(mi3p[i], mi3s[i+1]))), key=lambda x: x[0]*log(2)+x[1]*log(3))
for (a, b), (c, d) in result: print(a, b, c, d)