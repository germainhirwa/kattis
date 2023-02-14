import sys

for line in sys.stdin:
    n = int(line)
    s = list(input().strip())
    for e, i in enumerate(s):
        if '!' <= i <= '*' or '[' <= i <= ']':
            s[e] = '\\'*(2**n-1) + s[e]
    print(''.join(s))