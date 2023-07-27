import sys; input = sys.stdin.readline
n = int(input())
w = [input().strip() for _ in range(n)]
h = {}; d = 1e9
for i in range(n):
    if w[i] in h: d = min(d, i-h[w[i]])
    h[w[i]] = i
print(max(n-d, 0))