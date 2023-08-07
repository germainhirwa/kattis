for _ in range(int(input())):
    n = int(input()); b = 0
    while n: b = max(b, bin(n).count('1')); n //= 10
    print(b)