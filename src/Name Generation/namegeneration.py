from string import *
n = int(input())
v = {*'aeiou'}; c = {*ascii_lowercase}-v
a = []
for p in c:
    for q in c:
        for r in c:
            for s in c:
                for t in v:
                    if len({p, q, r, s}) != 4: continue
                    a.append((p+q+t+r+s+t)*3)
                    if len(a) == n:
                        for i in a: print(i)
                        exit(0)