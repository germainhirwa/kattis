n, p = int(input()), list(map(int, input().split()))
l, h = 2**-0.25, 2**-0.75
have, tape = 0, -l-h
target = 1<<31
area = target//2
for i in range(n-1):
    if i % 2 == 0: l /= 2
    else: h /= 2
    take = min((target-have)//area, p[i])
    have += take*area
    tape += take*(l+h)
    area //= 2
if have != target: print('impossible')
else: print(tape)