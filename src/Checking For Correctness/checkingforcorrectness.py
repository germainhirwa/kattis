import sys
for l in sys.stdin:
    a, op, b = l.split(); a, b = int(a), int(b)
    if op == '^': print(pow(a, b, 10000))
    else: print(eval(l.strip())%10000)