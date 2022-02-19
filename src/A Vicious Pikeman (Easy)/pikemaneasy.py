n, t, a, b, c, t0 = *list(map(int, input().split())), *list(map(int, input().split()))
arr = [t0]
for _ in range(n - 1):
    arr.append((a * arr[-1] + b) % c + 1)
arr.sort()

s, p, a = 0, 0, 0
for i in arr:
    if s + i <= t:
        s += i
        p += s
        a += 1
    else:
        break
print(a, p % 1000000007)