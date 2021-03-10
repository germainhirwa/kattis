import sys

first_line = False
for line in sys.stdin:
    if not first_line:
        n = int(line)
        first_line = True
        cups = []
    else:
        line = line.strip().split(" ")
        try:
            line[0] = int(line[0])
        except:
            cups.append((int(line[1]),line[0]))
        else:
            cups.append((int(line[0])//2,line[1]))

cups.sort()
for k,v in cups:
    print(v)