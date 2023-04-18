n, f = int(input()), 1
if n > 11: print('JUST RUN!!')
else:
    for _ in range(2, n+1): f *= _
    c = f
    for i in range(1, n):
        f //= i
        c += f
    print(c)