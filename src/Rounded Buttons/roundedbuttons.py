import sys; input = sys.stdin.readline
for _ in range(int(input())):
    x, y, w, h, r, n, *p = [*map(float, input().split())]; n = int(n)
    p = [(p[2*i], p[2*i+1]) for i in range(n)]
    for xx, yy in p:
        if x <= xx <= x+w:
            if y <= yy <= y+h:
                if x <= xx <= x+r and y <= yy <= y+r: print(['outside', 'inside'][(x+r-xx)**2+(y+r-yy)**2<=r**2])
                elif x <= xx <= x+r and y+h-r <= yy <= y+h: print(['outside', 'inside'][(x+r-xx)**2+(y+h-r-yy)**2<=r**2])
                elif x+w-r <= xx <= x+w and y <= yy <= y+r: print(['outside', 'inside'][(x+w-r-xx)**2+(y+r-yy)**2<=r**2])
                elif x+w-r <= xx <= x+w and y+h-r <= yy <= y+h: print(['outside', 'inside'][(x+w-r-xx)**2+(y+h-r-yy)**2<=r**2])
                else: print('inside')
            else: print('outside')
        else: print('outside')
    print()