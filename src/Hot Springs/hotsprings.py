from collections import deque
n, arr = int(input()), deque(sorted(map(int, input().split())))
res = []
while arr:
    res.append(arr.pop())
    if arr:
        res.append(arr.popleft())
print(*res[::-1])