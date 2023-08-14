import sys; input = sys.stdin.readline
t = int(input())
s = [int(input()) for _ in range(t)]
for a in range(10001):
    for b in range(10001):
        v = [s[0]]
        for i in range(1, t):
            if s[i] != (n:=(a*a*v[-1]+a*b+b)%10001): break
            v.append(n)
        if len(v) == t:
            for i in range(t): print((a*v[i]+b)%10001)
            exit(0)