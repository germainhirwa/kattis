n = int(input())
a = [*map(int, input().split())]
best = 0
for i in range(n-1):
    for j in range(i+1, n):
        p = [a[i], a[j]]
        k = j+1
        while k < n:
            if a[k] == p[-1]+p[-2]: p.append(a[k])
            k += 1
        best = max(best, len(p))
print(best)