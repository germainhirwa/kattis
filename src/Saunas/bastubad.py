n = int(input())
arr = []

def f(a, b, c, x):
    return a*x**2 + b*x + c

aa, bb, cc = 0, 0, 0
for _ in range(n):
    a, b, c, t = map(int, input().split())
    aa += a
    bb += b
    cc += c
    arr.append((a, b, c, t))
m = 0
arr.sort(key=lambda x: x[-1])
tt = [0] + list(map(lambda x: x[-1], arr))

for i in range(n):
    if aa == 0:
        if bb > 0:
            k = f(aa, bb, cc, tt[i+1])
        else:
            k = f(aa, bb, cc, tt[i])
    elif aa < 0:
        p = -bb/(2*aa)
        if tt[i] <= p <= tt[i+1]:
            k = f(aa, bb, cc, p)
        else:
            k = max(f(aa, bb, cc, tt[i]), f(aa, bb, cc, tt[i+1]))
    else: # aa > 0
        k = max(f(aa, bb, cc, tt[i]), f(aa, bb, cc, tt[i+1]))
    aa -= arr[i][0]
    bb -= arr[i][1]
    cc -= arr[i][2]
    m = max(m, k)

print(m)