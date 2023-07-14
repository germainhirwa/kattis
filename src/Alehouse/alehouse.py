import sys; input = sys.stdin.readline
ev = []
n, k = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    ev.append((a, 1)), ev.append((b+k, -1))
ev.sort(key=lambda x: (x[0], -x[1]))
best = curr = 0
for t, i in ev:
    curr += i
    best = max(best, curr)
print(best)