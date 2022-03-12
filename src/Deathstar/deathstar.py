n = int(input())
m = [0] * n
for i in range(n):
    arr = list(map(int, input().split()))
    for r in arr:
        m[i] |= r
print(*m)