import sys; input = sys.stdin.readline
hh = aa = mm = 0; dh = [0]*1920
for _ in range(int(input())):
    t, p, hm = input().split(); h, m = map(int, hm.split(':'))
    dh[60*h+m] += (1-2*(t>'A'))*int(p)
for ds in dh:
    mm += ds
    if mm < 0: hh += 1
    elif mm > 0: aa += 1
print('AH'[mm<0], f'{hh//60}:{str(hh%60).zfill(2)}', f'{aa//60}:{str(aa%60).zfill(2)}')