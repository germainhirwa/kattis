def f(n):
    if n == 0: return '{}'
    return '{' + ','.join(f(i) for i in range(n)) + '}'
print(f(int(input())))