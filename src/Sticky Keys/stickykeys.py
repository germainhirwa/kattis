r = []
for i in input():
    if not r or r[-1] != i: r.append(i)
print(''.join(r))