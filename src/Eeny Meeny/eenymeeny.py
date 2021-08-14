import sys

fl, sl = True, True
a, b = [], []

for line in sys.stdin:
    if fl:
        fl = False
        w = len(line.split(" "))
    elif sl:
        sl = False
        names = []
    else:
        names.append(line.strip())

while names:
    for i in range(w-1):
        names.append(names.pop(0))
    a.append(names.pop(0))

    if names:
        for i in range(w-1):
            names.append(names.pop(0))
        b.append(names.pop(0))

print(len(a))
for n in a:
    print(n)

print(len(b))
for n in b:
    print(n)
