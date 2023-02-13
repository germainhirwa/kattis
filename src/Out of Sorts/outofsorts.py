n, m, a, c, x0 = map(int, input().split())
arr = []
for _ in range(n):
    x0 = (a*x0 + c)%m
    arr.append(x0)
def bs(x):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo + hi)//2
        if arr[mid] == x: return True
        elif arr[mid] < x: lo = mid+1
        else: hi = mid-1
    return False
print(sum(map(bs, arr)))