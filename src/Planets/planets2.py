import sys; input = sys.stdin.readline
d = {}; h = {}
for _ in range(int(input())): c, _, *s = input().strip().split(); d[c] = s
for _ in range(int(input())): a, s = input().strip().split(); h[s] = h.get(s, 0) + int(a)
for i in sorted(d): print(i, sum(h[j] if j in h else 0 for j in d[i]))