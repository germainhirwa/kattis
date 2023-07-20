import sys; input = sys.stdin.readline
for _ in range(int(input())):
    b, k = map(int, input().split())
    a = i = 1; b -= 1
    while i <= k and i*i <= b:
        if b % i == 0:
            a = max(a, i)
            if b//i <= k: a = max(a, b//i)
        i += 1
    print(a)