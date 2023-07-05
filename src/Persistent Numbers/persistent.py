import sys
for l in sys.stdin:
    n = int(l)
    if n == -1: break
    if n < 10: print(n+10); continue
    pf = {i:0 for i in range(2, 10)}
    for i in range(9, 1, -1):
        while n % i == 0: n//=i; pf[i]+=1
    if n != 1: print('There is no such number.'); continue
    for i in range(2, 10): print(str(i)*pf[i], end='')
    print()