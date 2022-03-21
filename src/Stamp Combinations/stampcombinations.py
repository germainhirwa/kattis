import sys
m, n = map(int, input().split())
arr = tuple(map(int, input().split()))
ss = sum(arr)

def check(arr, s):
    if s == 0:
        return 'Yes'
    
    d, p = {0}, 0
    
    for el in arr:
        p += el
        if p - s in d:
            return 'Yes'
        d.add(p)
    return 'No'
    
for line in sys.stdin:
    print(check(arr, ss - int(line)))
