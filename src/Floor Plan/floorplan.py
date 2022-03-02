n = int(input())
if n % 4 == 2:
    print("impossible")
elif n % 2:
    print((n + 1) // 2, (n - 1) // 2)
else:
    print((n // 4 + 1), (n // 4 - 1))