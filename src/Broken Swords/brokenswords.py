import sys

tb, lr = 0,0

fl = False
for line in sys.stdin:
    if not fl:
        fl = True
    else:
        if line[0] == '0':
            tb += 1
        if line[1] == '0':
            tb += 1
        if line[2] == '0':
            lr += 1
        if line[3] == '0':
            lr += 1

k = min(tb,lr)//2
print(k,tb-2*k,lr-2*k)