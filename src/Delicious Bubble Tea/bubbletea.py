n, p, m, t = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))
s, x = min(min(map(lambda x: p[i]+t[x-1], list(map(int, input().split()))[1:])) for i in range(n)), int(input())
print(max(x//s-1, 0))