ops = ["+","-","*","//"]

data = {}

for a in ops:
    for b in ops:
        for c in ops:
            k = eval(f"4 {a} 4 {b} 4 {c} 4")
            data[k] = f"4 {a} 4 {b} 4 {c} 4 = {k}".replace("//","/")

import sys

fl = True
for line in sys.stdin:
    if fl:
        fl = False
    else:
        print(data.get(int(line),"no solution"))