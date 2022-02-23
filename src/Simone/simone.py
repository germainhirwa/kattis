n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
freq = [100000] + [0] * k
for i in range(n):
    freq[arr[i]] += 1
minfreq = min(freq)

res = list(filter(lambda x: freq[x] == minfreq, range(1, k + 1)))
print(len(res))
print(*res)