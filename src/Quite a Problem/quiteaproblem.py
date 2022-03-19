import sys

for line in sys.stdin:
    print('yes' if line.lower().find('problem') != -1 else 'no')