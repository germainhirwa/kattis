import sys

for i, line in enumerate(sys.stdin):
    tokens = line.split()
    stack = []
    for token in tokens:
        stack.append(token)
        while len(stack) > 2 and stack[-1].replace('-','').isdigit() and stack[-2].replace('-','').isdigit() and stack[-3] in '+-*':
            o2, o1, op = stack.pop(), stack.pop(), stack.pop()
            stack.append(str(eval(o1+op+o2)))
    print(f"Case {i+1}: {' '.join(stack)}")