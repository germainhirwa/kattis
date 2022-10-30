n, s = int(input()), input()
a, c = 0, 0
for i in range(n):
    if s[i] == '1':
        a += 1
        c = min(2, c + 2)
    else:
        if c > 0:
            a += 1
            c -= 1
print(a)