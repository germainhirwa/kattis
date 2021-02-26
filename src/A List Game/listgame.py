n = int(input())
k = 0
i = 2
while i**2 <= n:
    if n%i == 0:
        n //= i
        k += 1
    else:
        i += 1
print(k + (0 if n == 1 else 1))