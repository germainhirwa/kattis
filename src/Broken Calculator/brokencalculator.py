import sys
r = [1, input()][0]
for l in sys.stdin:
    a, op, b = l.split()
    a, b = int(a), int(b)
    if op == '+':   r = a+b-r
    elif op == '-': r *= (a-b)
    elif op == '*': r = (a*b)**2
    else:           r = (a+1)//2
    print(r)