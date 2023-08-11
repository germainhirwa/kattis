n = int(input()); a = [*map(int, input().split())]; s = sum(a); t = s//2; m = {0}
if s%2: print('NO'), exit(0)
for i in a:
    for j in [*m]: m.add(i+j)
    if t in m: print('YES'), exit(0)
print('NO')