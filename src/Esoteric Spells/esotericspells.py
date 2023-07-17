import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n, arr, x = int(input()), [*map(int, input().split())], 0; s = [0]*n
    for i in range(60):
        k = 1<<(59-i)
        for j in range(n):
            if arr[j] >= k: s[j] += k; arr[j] -= k; break
    for i in range(n): x ^= s[i]
    print(x), print(*s)