n, p = map(int, input().split())
arr = list(map(lambda x: int(x) - p, input().split()))

# Kadane's Algorithm
lm = [arr[0]] * n
for i in range(1, n):
    lm[i] = max(arr[i], lm[i - 1] + arr[i])
print(max(lm))