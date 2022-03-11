c = int(input())
for idx in range(1, c + 1):
    n, t = map(int, input().split())
    e = int(input())
    hp = []
    for _ in range(n):
        hp.append([])
    for _ in range(e):
        h, p = map(int, input().split())
        if h != t:
            hp[h - 1].append(p)
    def do():
        for i in range(n):
            if sum(hp[i]) < len(hp[i]):
                print(f'Case #{idx}: IMPOSSIBLE')
                return
            hp[i].sort(reverse=True)
        cc = [0] * n
        for i in range(n):
            s = len(hp[i])
            while s > 0:
                s -= hp[i][cc[i]]
                cc[i] += 1
        print(f'Case #{idx}:', *cc)
        return
    do()