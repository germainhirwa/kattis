import sys

d = {}
for line in sys.stdin:
    line2 = line.strip().split()
    for i in range(len(line2)):
        if line2[i].lower() in d:
            line2[i] = "."
        else:
            d[line2[i].lower()] = 1
    print(" ".join(line2))