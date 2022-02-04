import sys

skip = input()

def check(s):
    stack = []
    for c in s:
        if c in ['$', '|', '*']:
            stack.append(c)
        elif c == 't':
            if not stack or stack[-1] != '|':
                return 'NO'
            stack.pop()
        elif c == 'j':
            if not stack or stack[-1] != '*':
                return 'NO'
            stack.pop()
        elif c == 'b':
            if not stack or stack[-1] != '$':
                return 'NO'
            stack.pop()
    if not stack:
        return 'YES'
    return 'NO'

for line in sys.stdin:
    print(check(line.strip()))