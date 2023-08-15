n = int(input())
if n > 17: print('0.6321205588285578'), exit(0)
f = m = p = 1
for i in range(n+1):
    p -= m/f
    m = -m
    f *= i+1
print(p)