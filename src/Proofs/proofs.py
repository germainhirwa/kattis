import sys

fl, ok = True, True
l, x = 1, -1
k = {}
for line in sys.stdin:
    if fl:
        fl = False
        continue

    line = line.strip()
    if line[:2] == "->":
        for w in line[3:].split(" "):
            k[w] = l
    else:
        s = line.split(" ")
        ar = s.index("->")
        for a in s[:ar]:
            if a not in k:
                ok = False
                x = l
        if not ok:
            break
        else:
            for c in s[ar+1:]:
                k[c] = l
    l += 1

if ok:
    print("correct")
else:
    print(x)