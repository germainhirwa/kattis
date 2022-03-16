t = int(input())
for _ in range(t):
    d, n = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = [0]
    for i in range(len(arr)):
        arr2.append((arr2[-1] + arr[i]) % d)
    freq = {}
    for k in arr2:
        if k not in freq:
            freq[k] = 0
        freq[k] += 1
    print(sum(map(lambda x: x * (x - 1) // 2, freq.values())))