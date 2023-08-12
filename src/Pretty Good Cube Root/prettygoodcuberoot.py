import sys
for l in sys.stdin:
    l = int(l)
    hi = int(10**(500/3)+10)
    lo = -hi
    while hi-lo>1:
        mi = (lo+hi)//2
        if mi**3 < l: lo = mi
        else: hi = mi
    print(min([mi-2, mi-1, mi, mi+1, mi+2], key=lambda x: abs(x**3-l)))