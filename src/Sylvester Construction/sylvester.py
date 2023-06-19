for _ in range(int(input())):
    n, x, y, w, h = map(int, input().split())
    b = len(bin(n))-3
    for i in range(h):
        for j in range(w):
            u, v, p = x+j, y+i, n//2
            m3 = 0
            for _ in range(b):
                m3 += (u >= p and v >= p)
                u %= p
                v %= p
                p //= 2
            print(1-2*(m3%2), end=' ')
        print()
    print()