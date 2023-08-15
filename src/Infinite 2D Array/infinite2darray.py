'''
Let f_0 = 0 and f_1 = 1 be the first two terms of the Fibonacci sequence.
F_(x,y) = sum(f_i * C(x+y-1-i, y-1) for i in [1..x]) + sum(f_i * C(x+y-1-i, x-1) for i in [1..y])
Example:
F_(4,5) = 70f_1 + 35f_2 + 15f_3 + 5f_4 + f_5
        = (7C4+7C3)f_1 + (6C4+6C3)f_2 + (5C4+5C3)f_3 + (4C4+4C3)f_4 + (3C3)f_5
        = (7C4*f_1 + 6C4*f_2 + 5C4*f_3 + 4C4*f_4) + (7C3*f_1 + 6C3*f_2 + 5C3*f_3 + 4C3*f_4 + 3C3*f_5)
'''
from array import array
x, y = map(int, input().split()); MOD = 10**9+7
f = array('i', [1]); fib = array('i', [0, 1])
for i in range(x+y-1): f.append(f[-1]*(i+1)%MOD)
for _ in range(max(x,y)-1): fib.append((fib[-1]+fib[-2])%MOD)
p = array('i', [fib[i]*f[x+y-1-i]%MOD for i in range(max(x,y)+1)])
inv = array('i', [pow(f[i], -1, MOD) for i in range(max(x,y))]); ans = 0
for i in range(1, x+1): ans += p[i]*inv[y-1]*inv[x-i]
for i in range(1, y+1): ans += p[i]*inv[x-1]*inv[y-i]
print(ans%MOD)