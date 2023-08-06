for _ in range(int(input())):
    n = int(input())
    if n == 1: print(1), print(1)
    elif n == 2: print(1), print(2)
    elif n % 4 == 0: print(n), print(*range(1, n+1))
    elif n % 4 == 1: print(n-1), print(*range(1, n-1), n)
    elif n % 4 == 2: print(n-1), print(*range(2, n+1))
    else: print(n-1), print(*range(1, n))