s = input()
d = {}
can = True

for l in s:
    if l in d:
        can = False
    d[l] = True

print(int(can))