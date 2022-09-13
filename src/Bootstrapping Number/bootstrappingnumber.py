n = int(input())
lo, hi = 1, 10
while abs(hi - lo) >= 1e-7:
    mid = (lo + hi) / 2
    exp = mid**mid
    if exp == n:
        break
    elif exp < n:
        lo = mid
    else:
        hi = mid
print(mid)