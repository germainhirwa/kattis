import sys

c = [1]*5000
for i in range(1,5000):
    c[i] = c[i-1]*(4*i+2)
    c[i] //= (i+2)

first_line = False
for line in sys.stdin:
    if not first_line:
        first_line = True
    else:
        print(c[int(line)-1])