import sys

fl = False
for line in sys.stdin:
    if not fl:
        fl = True
        if int(line) == 1:
            print(1)
            sys.exit(0)
        r = ["1"]
    else:
        l = list(map(int,line.split()))
        r += ["0"]*len(l)
        for i in range(len(l)):
            r[l[i]+1] = str(i+2)

print(" ".join(r))