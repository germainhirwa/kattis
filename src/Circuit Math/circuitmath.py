import sys

fl = False
sl = False

for line in sys.stdin:
    if not fl:
        n = int(line)
        fl = True
    elif not sl:
        bools = list(map(lambda x:x=='T',line.split()))
        sl = True
    else:
        exp = line.split()
        stack = []
        for i in exp:
            if 65 <= ord(i) <= 90:
                stack.append(bools[ord(i)-65])
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a and b)
            elif i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a or b)
            else:
                stack.append(not stack.pop())
        print('T' if stack.pop() else 'F')