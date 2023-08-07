import sys; input = sys.stdin.readline
while True:
    n, *r = map(int, input().split())
    if n == 0: break
    s = [*input().strip()]
    while len(s) % n: s.append(' ')
    t = s.copy()
    for i in range(len(s)//n):
        for j in range(n): t[i*n+j] = s[i*n+r[j]-1]
    print("'"+''.join(t)+"'")