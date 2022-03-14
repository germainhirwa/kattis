import sys
input()

for line in sys.stdin:
    print(' '.join(list(str(int(''.join(line.split())) + int(''.join(input().split()))))))