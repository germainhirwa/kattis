b, n, e = list(map(int, input().split()))
s = list(map(int, input().split()))
vc = list(map(int, input().split()))
vc.sort()
m = len(vc) # (b + n + e) // 2

lo, hi = 0, 10**9
def possible(speed): # can we assign such that the minimum speed is $speed?
    left = [b, n, e]
    used = [False] * m
    for i in range(3):
        for j in range(3):
            for k in range(m):
                if used[k]:                         continue # used kayak
                if i == j and left[i] < 2:          continue # bb/ee/nn not possible
                if 0 in [left[i], left[j]]:         continue # either b e or n no more
                if vc[k] * (s[i] + s[j]) < speed:   continue # violating PS
                # kind of greedy approach since we want to find the first pair from bb to ee that satisfies the speed constraint
                # probably for bb will be satisfied once vc[k] is large enough and ee when vc[k] is still small, interesting :)
                used[k] = True
                left[i] -= 1
                left[j] -= 1
    return sum(left) == 0


while hi - lo != 1:
    mid = (lo + hi) // 2
    if possible(mid):
        lo = mid
    else:
        hi = mid
print(lo)