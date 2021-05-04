import sys

fl = True
for line in sys.stdin:
    if fl:
        fl = False
    else:
        he = sorted(list(map(int,line.split(" "))))
        m = 1
        for i in range(len(he)):
            if he[i] > (i+1):
                print("impossible")
                sys.exit(0)
            else:
                m = min(m,he[i]/(i+1))
        print(m)