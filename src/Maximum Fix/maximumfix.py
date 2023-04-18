n, f = int(input()), {}
for w in [(i-e)%n for i, e in enumerate(map(lambda x: int(x)-1, input().split()))]:
    if w not in f: f[w] = 0
    f[w] += 1
print(*max(f.items(), key=lambda x: (x[1], -x[0])))