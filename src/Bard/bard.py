import sys; input = sys.stdin.readline
n, e = int(input()), int(input()); d = []
for _ in range(e): _, *r = map(int, input().split()); d.append({*r})
k = [set() for _ in range(n)]
for r in d:
    if 1 in r:
        s = len(k[0])
        for w in r: k[w-1].add(s)
    else:
        b = set()
        for w in r: b |= k[w-1]
        for w in r: k[w-1] = b.copy()
for i in range(n):
    if len(k[i]) == len(k[0]): print(i+1)