for _ in range(int(input())):
    h = {}
    for _ in range(int(input())):
        n, q = input().split()
        if n not in h: h[n] = 0
        h[n] += int(q)
    print(len(h))
    for (n, q) in sorted(h.items(), key=lambda x: (-x[1], x[0])): print(n, q)