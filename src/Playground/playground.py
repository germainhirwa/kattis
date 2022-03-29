import sys

n = None
for line in sys.stdin:
    if n == None:
        n = int(line)
    else:
        arr = sorted(map(float, line.split()))
        s = arr[0]
        ok = False
        for i in range(1, n):
            if s >= arr[i]:
                ok = True
                break
            s += arr[i]
        print('YES' if ok else 'NO')
        n = None