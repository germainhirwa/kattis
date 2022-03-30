import sys

def convert(c):
    return {'0': ' ', '<': ',', '>': '.'}[c]

def correct(s):
    if s == '!':
        return s.replace('!', '-.')
    return s

s, a = input().split()
offset = sum(map(lambda x: ord(x) - 32, correct(s))) - ord(a)
for line in sys.stdin:
    line = line.strip().split()
    print(''.join(map(lambda x: chr(sum(map(lambda y: ord(y) - 32, correct(x))) - offset) if x not in ['0', '>', '<'] else convert(x), line)))