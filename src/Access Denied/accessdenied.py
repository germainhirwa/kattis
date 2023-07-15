from string import *; print('0'); cur = [0]
while True:
    if (verdict:=input().split())[1][0] > 'D': exit(0)
    if (time:=int(verdict[2][1:])) == 5: cur.append(0)
    else: cur[(time-14)//9] += 1
    print(''.join(printable[i] for i in cur))