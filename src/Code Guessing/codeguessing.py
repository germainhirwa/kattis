a1, a2 = map(int, input().split())
possible = []
arr = list(input())

arr[arr.index('A')] = a1
arr[arr.index('A')] = a2

for i in range(1, 10):
    for j in range(1, 10):
        arr2 = arr.copy()
        arr2[arr2.index('B')] = i
        arr2[arr2.index('B')] = j
        if sorted(arr2) == arr2 and len(set(arr2)) == 4:
            possible.append((i, j))
if len(possible) == 1:
    print(*possible[0])
else:
    print(-1)