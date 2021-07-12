import sys

entry = {}
t = int(input())

for line in sys.stdin:
    c, n = line.strip().split(" ")
    if c == 'entry':
        if not entry.get(n, False):
            print(f'{n} entered')
            entry[n] = True
        else:
            print(f'{n} entered (ANOMALY)')
    else:
        if entry.get(n, False):
            print(f'{n} exited')
            entry[n] = False
        else:
            print(f'{n} exited (ANOMALY)')