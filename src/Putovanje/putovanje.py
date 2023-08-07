import sys; input = sys.stdin.readline
N, C = map(int, input().split())
W = [*map(int, input().split())]
best = 0
for i in range(N):
    curr = freq = 0
    for j in range(i, N):
        if curr + W[j] <= C: curr += W[j]; freq += 1
    best = max(best, freq)
print(best)