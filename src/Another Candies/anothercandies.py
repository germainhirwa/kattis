t = int(input())
for _ in range(t):
    skip = input()
    n = int(input())
    s = 0
    for _ in range(n):
        s += int(input())
    print(['NO', 'YES'][int(s % n == 0)])