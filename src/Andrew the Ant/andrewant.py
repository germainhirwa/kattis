import sys

for line in sys.stdin:
    l, a = list(map(int, line.split()))
    left = 0
    maxl, maxr = -1, -1
    arr = []
    for _ in range(a):
        pos, dir = input().split()
        pos = int(pos)
        if dir == 'L':
            left += 1
            maxl = max(maxl, pos)
        else:
            maxr = max(maxr, l - pos)
        arr.append(pos)
    arr.sort()

    if maxl == maxr:
        print(f'The last ant will fall down in {max(maxl, maxr)} seconds - started at {arr[left - 1]} and {arr[left]}.')
    elif maxl > maxr:
        print(f'The last ant will fall down in {max(maxl, maxr)} seconds - started at {arr[left - 1]}.')
    else:
        print(f'The last ant will fall down in {max(maxl, maxr)} seconds - started at {arr[left]}.')