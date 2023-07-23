import sys; input = sys.stdin.readline
n, p = map(int, input().split())
a = sorted(map(int, input().split()))
m = 0
for i in range(n): m = max(m, p*(i+1)-a[i])
print(m+a[0])