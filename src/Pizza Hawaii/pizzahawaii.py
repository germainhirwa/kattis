from collections import defaultdict
for _ in range(int(input())):
    m1, m2 = defaultdict(list), defaultdict(list)
    for i in range(int(input())):
        input(); a, b = input().split()[1:], input().split()[1:]
        for j in a: m1[j].append(i)
        for j in b: m2[j].append(i)
    p = []
    for i in m1:
        for j in m2:
            if m1[i] == m2[j]: p.append((i, j))
    for a, b in sorted(p): print(f'({a}, {b})')
    print()