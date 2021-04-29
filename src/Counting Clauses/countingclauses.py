import sys

for line in sys.stdin:
    s = list(map(int,line.split(" ")))
    if len(s) == 2 and s[0] >= 8:
        print("satisfactory")
    else:
        print("unsatisfactory")
    sys.exit(0)