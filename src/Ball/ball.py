import sys; input = sys.stdin.readline
m = set(); a = b = None
for _ in range(int(input())//2+1):
    x, y = map(int, input().split())
    if x in m:
        if a == None: a = x
        else: b = x
    if y in m:
        if a == None: a = y
        else: b = y
    m.add(x), m.add(y)
print(min(a, b), max(a, b))