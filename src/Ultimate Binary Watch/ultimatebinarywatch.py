s = input()
m = []

for i in s:
    k = bin(int(i))[2:]
    m.append('0' * (4 - len(k)) + k)
m = list(map(list, zip(*m)))

for i in range(4):
    for j in range(4):
        m[i][j] = '.' if m[i][j] == '0' else '*'
    print(f"{' '.join(m[i][:2])}   {' '.join(m[i][2:])}")