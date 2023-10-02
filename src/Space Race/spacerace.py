n = int(input())
d = float(input())
l = [input().split() for _ in range(n)]
print(min(l, key=lambda x: float(x[2]))[0])