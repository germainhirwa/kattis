fibs, n = [1, 2], int(input())
while fibs[-1] <= n:
    fibs.append(fibs[-1] + fibs[-2])
ans = []
while fibs:
    u = fibs.pop()
    if u <= n:
        ans.append(u)
        n -= u
print(*ans[::-1])