import sys

lo = 1
mid = 1
hi = 1000

while lo <= hi:
    mid = (hi+lo)//2
    print(mid)
    verdict = input()
    if verdict == "correct":
        sys.exit(0)
    elif verdict == "lower":
        hi = mid-1
    else: # higher
        lo = mid+1