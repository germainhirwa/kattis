from itertools import *
p = [[*map(int, input().split())] for _ in range(3)]
for (h1, w1), (h2, w2), (h3, w3) in permutations(p):
    for _ in range(2):
        for _ in range(2):
            for _ in range(2):
                if h1==h2==h3 and w1+w2+w3==h1: print('YES'), exit(0)
                if h1==h2 and w3==w1+w2==h1+h3: print('YES'), exit(0)
                h1, w1 = w1, h1
            h2, w2 = w2, h2
        h3, w3 = w3, h3
print('NO')