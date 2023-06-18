for _ in range(int(input())):
    n, m = map(int, input().split())
    t = []
    for _ in range(n):
        k, *nn, p = map(int, input().split())
        t.append([nn, p])
    a = list(map(int, input().split()))
    z = 0
    for (nn, p) in t: z += p*min(map(lambda x: a[x-1], nn))
    print(z)