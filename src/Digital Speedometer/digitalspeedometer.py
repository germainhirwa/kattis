import sys
l, r = float(input()), float(input())
O = []
for s in sys.stdin:
    s = float(s); f = s-int(s); k = int(s)
    if 0 < s < 1: print(1)
    elif f <= l: print(k)
    elif f >= r: print(k+1)
    else:
        for i in range(len(O)-1, -1, -1):
            if k+l <= O[i] <= k+r: continue
            print(k+(O[i]>k+r)); break
    O.append(s)