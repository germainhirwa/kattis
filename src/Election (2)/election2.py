from collections import Counter
m = {}; c = Counter()
for _ in range(int(input())): s = input(); m[s] = input()
for _ in range(int(input())): c[input()] += 1
max_freq = max(c.values())
names = [i for i in c if c[i] == max_freq]
if len(names) > 1: print('tie')
else: print(m[names[0]])