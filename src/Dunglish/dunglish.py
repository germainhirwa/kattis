from collections import Counter
import sys; input = sys.stdin.readline
n = int(input())
ww = input().strip().split()
w = Counter(ww)
h = {}; t = {}
for _ in range(int(input())):
    p, s, c = input().split()
    if p not in h: h[p] = [0, 0]; t[p] = s
    h[p][c[0]!='i'] += 1
cc = aa = 1
for k in w: cc *= (h[k][0]+h[k][1])**w[k]; aa *= h[k][1]**w[k]
if cc > 1: print(aa, 'correct'), print(cc-aa, 'incorrect')
else: print(' '.join(t[i] for i in ww)), print(['incorrect', 'correct'][all(v[1] for v in h.values())])