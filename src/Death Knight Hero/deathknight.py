import sys

fl = True
k = 0
for line in sys.stdin:
    if fl:
        fl = False
    else:
        k += int('CD' not in line)

print(k)