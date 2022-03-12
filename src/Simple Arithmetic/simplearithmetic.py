def f(a, b, c):
    if a * b % c == 0:
        return a * b // c
    T = 20
    r = str(a * b * 10**T // c)
    r = '0' * (max(0, T - len(r))) + r
    if not r[:-T]:
        return '0.' + r[-T:]
    return r[:-T] + '.' + r[-T:]
    
a, b, c = map(int, input().split())
print(f(a, b, c))