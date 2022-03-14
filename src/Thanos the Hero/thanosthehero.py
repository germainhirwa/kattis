n = int(input())
arr = list(map(int, input().split()))[::-1]
possible = True
kill = 0
for i in range(1, n):
    if arr[i] >= arr[i - 1] >= 1:
        kill += arr[i] - arr[i - 1] + 1
        arr[i] = arr[i - 1] - 1
    elif arr[i - 1] == 0:
        possible = False
        break
print(kill + int(kill == 0) if possible else 1)