n, c, b = map(int, input().split())
z = list(map(int, input().split()))
r = [-1]*n
for i in z: r[i-1] = 0
r[0] = c % 2
for i in range(1, n-1):
    if r[i] == -1:
        if c > 0:   r[i], c = 1 - r[i-1], c-1
        else:       r[i] = 0
    elif r[i] != r[i-1]:
        c -= 1
print(''.join(map(lambda x: chr(x+48), r)))