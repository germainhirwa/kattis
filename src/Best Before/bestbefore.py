from datetime import *
from itertools import *
a, b, c = input().split('/')
can = []
for y, m, d in permutations((a, b, c)):
    y = y.zfill(3)
    if len(y) != 4: y = '2'+y
    try: can.append(datetime(int(y), int(m), int(d)))
    except: pass
if not can: print(f'{a}/{b}/{c} is illegal')
else: print(min(can).strftime('%Y-%m-%d'))