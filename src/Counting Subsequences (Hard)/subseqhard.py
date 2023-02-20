for _ in range(int(input())):
    input(), input()
    d, p, a = {0:1}, 0, 0
    for e in map(int, input().split()):
        p += e
        if p-47 in d: a += d[p-47]
        if p not in d: d[p] = 0
        d[p] += 1
    print(a)