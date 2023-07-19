m = 1; l = 0
for x, i in sorted([[*map(int, input().split())] for _ in range(int(input()))], key=lambda x: x[1]): l += max(0, x-m); m = max(m, x)+1
print(l)