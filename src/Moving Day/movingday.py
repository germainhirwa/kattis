n, v = map(int, input().split())
print(max((a:=[*map(int, input().split())])[0]*a[1]*a[2]-v for _ in range(n)))