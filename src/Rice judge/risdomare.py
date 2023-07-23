n = int(input())
p = input()>'b'
a = [[*map(int, input().split())] for _ in range(n)]
print(max(range(n), key=lambda i: (a[i][0]+a[i][1], a[i][p]))+1)