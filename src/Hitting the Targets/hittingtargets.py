import sys

targets = []

for line in sys.stdin:
    s = line.split(" ")
    if len(s) > 3:
        targets.append(list(map(int,s[1:])))
    elif len(s) == 2:
        h = 0
        x,y = list(map(int,s))
        for t in targets:
            if len(t) == 4: # rectangle
                h += int(t[0] <= x <= t[2] and t[1] <= y <= t[3])
            else: # circle
                h += int((x-t[0])**2 + (y-t[1])**2 <= t[2]**2)
        print(h)