from itertools import *
for _ in range(int(input())):
    a1, b1, a2, b2, a3, b3 = map(int, input().split())
    p = ((a1, b1), (a2, b2), (a3, b3)); m = float('inf')
    for (a1, b1), (a2, b2), (a3, b3) in permutations(p):
        for _ in range(2):
            for _ in range(2):
                for _ in range(2):
                    m = min(m, max(a1+a2,a3)*(max(b1,b2)+b3), (a1+a2+a3)*max(b1,b2,b3))
                    a3, b3 = b3, a3
                a2, b2 = b2, a2
            a1, b1 = b1, a1
    print(m)