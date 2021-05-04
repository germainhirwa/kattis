birthdays = {}

import sys

for line in sys.stdin:
    try:
        name, like, date = line.strip().split(" ")
        if date not in birthdays:
            birthdays[date] = (like,name)
        elif int(birthdays[date][0]) < int(like):
            birthdays[date] = (like,name)
    except:
        pass

print(len(birthdays))
for n in sorted(list(map(lambda x:x[1],birthdays.values()))):
    print(n)