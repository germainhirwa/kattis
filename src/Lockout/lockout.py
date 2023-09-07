import sys; input = sys.stdin.readline
n = int(input()); a = [*map(int, input().split())]; input(); p = [*map(int, input().split())]; s = sum(a)
if 2*a[p[0]-1] < s: print(1), print(*p[1:], p[0])
elif 2*a[p[0]-1] > s or n != 2: print(0.5), print(*p)
else: print(0.25), print(*p)