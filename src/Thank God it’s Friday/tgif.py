from datetime import *
d, m = input().split(); d = int(d)
m = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}[m]
w = {'MON':0, 'TUE':1, 'WED':2, 'THU':3, 'FRI':4, 'SAT':5, 'SUN':6}[input()]
c = set()
for y in range(1800, 2800):
    try:
        if datetime(y, 1, 1).weekday() == w: c.add(datetime(y, m, d).weekday())
    except: pass
if 4 not in c: print(':(')
elif len(c) == 1: print('TGIF')
else: print('not sure')