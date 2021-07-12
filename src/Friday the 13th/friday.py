import sys

fl = True
dm = True
for line in sys.stdin:
    if fl:
        fl = False
    else:
        if dm:
            dm = False
        else:
            w, fri = 6, 0
            days = list(map(int, line.split(" ")))
            print(days)
            for d in days:
                if (w+13) % 7 == 5:
                    fri += 1
                w = (w+d) % 7
            print(fri)
            dm = True