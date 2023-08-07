from collections import Counter
c1 = Counter(input()); c2 = Counter(input())
for i in c2:
    if c2[i] == 2*c1[i]: print(i, end='')