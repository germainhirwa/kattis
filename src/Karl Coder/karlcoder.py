buf = {}; s = x = 1
def get(x):
    if x not in buf: print(f'buf[{x}]'); buf[x] = int(input())
    return buf[x]
while True:
    if get(x) == 0: break
    x += s; s *= 2
lo, hi = 1, x
while hi-lo>1:
    mi = (lo+hi)//2
    if not get(mi): hi = mi
    else: lo = mi+1
ans = lo if not get(lo) else lo+1
print('strlen(buf) =', ans)