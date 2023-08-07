n, c = input().split(); n = int(n)
a = [*range(n)]; t = 1
while True:
    if c[0] == 'o': s = a[::2]+a[1::2]
    else: s = a[1::2]+a[::2]
    if s == [*range(n)]: break
    t += 1; a = s
print(t)