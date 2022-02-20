import sys
n, k = list(map(int, input().split()))
arr = []

for line in sys.stdin:
    a, b = list(map(int, line.split()))
    arr.append([b, a])
arr.sort()

assign = list(range(n))
final = list(range(n))
for i in range(k):
    pos = arr[i][1]
    assign[pos], assign[pos + 1] = assign[pos + 1], assign[pos]
for i in range(n):
    final[assign[i]] = i
print(*final)