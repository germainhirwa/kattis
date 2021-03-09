import sys
exp = ''
for line in sys.stdin:
    exp += line.strip()
print(eval(exp))