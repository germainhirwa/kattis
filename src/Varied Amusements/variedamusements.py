n, a, b, c = map(int, input().split()); MOD = 10**9+7
mem = {}
def f(n, l=-1):
    tup = (n, l)
    if tup in mem: return mem[tup]
    if n == 0: return 1
    s = 0
    if l == 0: s = b*f(n-1, 1) + c*f(n-1, 2)
    elif l == 1: s = a*f(n-1, 0) + c*f(n-1, 2)
    elif l == 2: s = a*f(n-1, 0) + b*f(n-1, 1)
    else:
        s = a*f(n-1, 0) + b*f(n-1, 1) + c*f(n-1, 2)
    mem[tup] = s%MOD; return s%MOD
print(f(n))