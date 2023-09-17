a, b = map(int, input().split()); s = []
for i in range(a, b+1):
    for j in range(i, b+1):
        if sorted(str(i)+str(j)) == sorted(str(i*j)): s.append((i, j))
print(f'{len(s)} digit-preserving pair(s)')
for x, y in s: print(f'x = {x}, y = {y}, xy = {x*y}')