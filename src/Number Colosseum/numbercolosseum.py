import sys; input = sys.stdin.readline
n, nums = int(input()), [*map(int, input().split())]
pve, nve = [], []
for i in nums:
    pve.append(i) if i > 0 else nve.append(i)
    while pve and nve:
        a, b = pve.pop(), nve.pop(); c = a+b
        if c > 0: pve.append(c)
        elif c < 0: nve.append(c)
if pve: print('Positives win!'), print(*pve)
elif nve: print('Negatives win!'), print(*nve)
else: print('Tie!')