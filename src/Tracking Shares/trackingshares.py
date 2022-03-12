D = [0] * 366
days = set()
c = int(input())
for _ in range(c):
    arr = []
    k = int(input())
    for _ in range(k):
        n, d = map(int, input().split())
        arr.append((d, n))
        days.add(d)
    arr.sort()
    for i in range(len(arr) - 1):
        s, e = arr[i][0], arr[i+1][0]
        for j in range(s, e):
            D[j] += arr[i][1]
    if arr:
        for j in range(arr[-1][0], 366):
            D[j] += arr[-1][1]
print(*list(map(lambda x: D[x], sorted(days))))