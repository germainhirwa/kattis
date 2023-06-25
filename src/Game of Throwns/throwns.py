n, k = map(int, input().split())
e, i, c = 0, 0, input().strip().split()
c2 = []
while i < len(c):
    if c[i] == 'undo':
        for _ in range(int(c[i+1])): c2.pop() if c2 else 0
        i += 2
    else: c2.append(int(c[i])); i += 1
print(sum(c2) % n)