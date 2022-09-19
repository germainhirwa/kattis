import sys
n = int(input())
w = []
for line in sys.stdin:
    w.append(list(map(int, line.split())))
lw, hw = min(map(min, w)), max(map(max, w))
w1, w2 = w

def check(lb):
    # Check if I have remaining unpaired
    w3 = list(filter(lambda x: x >= lb, w1))
    w4 = list(filter(lambda x: x >= lb, w2))
    for ww in w3, w4:
        if len(ww) % 2:
            return False, w3, w4
        for i in range(len(ww) // 2):
            if ww[2*i] != ww[2*i + 1]:
                return False, w3, w4
    return True, w3, w4

if check(0)[0]:
    print(0)
    sys.exit(0)

lo, hi = lw - 1, hw + 1
while hi - lo > 1:
    mid = (lo + hi) // 2
    r = check(mid)
    if r[0]:
        hi = mid
    else:
        lo = mid
        w1, w2 = r[1:]
print(lo)