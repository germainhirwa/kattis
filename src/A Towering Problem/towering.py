*a, h1, h2 = [*map(int, input().split())]
for i in range(64):
    if bin(i).count('1') != 3: continue
    c = [[], []]
    for j in range(6):
        if i&(1<<j): c[1].append(a[j])
        else: c[0].append(a[j])
    if [*map(sum, c)] == [h1, h2]: print(*sorted(c[0])[::-1], *sorted(c[1])[::-1]), exit(0)