n = int(input())
t = list(map(int, input().split(" ")))

minmax_t = max(t[0], t[2])
minmax_idx = 0
for i in range(n-2):
    if max(t[i], t[i+2]) < minmax_t:
        minmax_t = max(t[i], t[i+2])
        minmax_idx = i
print(minmax_idx + 1, minmax_t)