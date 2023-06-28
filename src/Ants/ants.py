for _ in range(int(input())):
    l, n = map(int, input().split())
    a = []
    while len(a) != n: a.extend(map(int, input().split()))
    print(max(min(i, abs(i-l)) for i in a), max(max(i, abs(i-l)) for i in a))