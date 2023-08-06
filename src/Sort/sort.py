from collections import Counter
N, C = map(int, input().split())
a = [*map(int, input().split())]
c = Counter(a)
for i, f in sorted(c.items(), key=lambda x: -x[1]):
    for _ in range(f): print(i, end=' ')