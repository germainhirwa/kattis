import sys; input = sys.stdin.readline
n = int(input()); a = [*map(int, input().split()), 0]
print(sum(max(a[i]-a[i+1]-1, 0) for i in range(n)))