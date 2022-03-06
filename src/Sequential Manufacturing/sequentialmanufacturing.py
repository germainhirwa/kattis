n, p = map(int, input().split())
t = list(map(int, input().split()))
print(sum(t) + (p - 1) * max(t))