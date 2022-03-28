dd = [list(map(int, input().split()[1:]))]
common = (len(set(dd[-1])) == 1)

while not common:
    temp = []
    vals = set()
    for i in range(1, len(dd[-1])):
        temp.append(dd[-1][i] - dd[-1][i - 1])
        vals.add(temp[-1])
    common = (len(vals) == 1)
    dd.append(temp)

for i in range(len(dd) - 2, -1, -1):
    dd[i].append(dd[i][-1] + dd[i + 1][-1])
print(len(dd) - 1, dd[0][-1])