r, f = map(int, input().split())
print(['up', 'down'][round(f/r)%2])