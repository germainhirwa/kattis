import sys
n, names = int(input()), []
for l in sys.stdin: names.append(l.strip())

if names[0] == 'ThoreHusfeldt': print('Thore is awesome')
else:
    pos = names.index('ThoreHusfeldt')
    for i in range(pos):
        if names[i].startswith('ThoreHusfeld'):
            print('Thore sucks'), sys.exit(0)
    prefix, best = ['ThoreHusfeld'[:i] for i in range(13)], 0
    for i in range(pos):
        for j in range(best, 13):
            if not names[i].startswith(prefix[j]): best = j; break
    print(prefix[best])