import sys

for logic in sys.stdin:
    logic = logic.strip()
    if logic == '0':
        break

    def check():
        for p in ((0, 1), (1,))[logic.find('p') == -1]:
            for q in ((0, 1), (1,))[logic.find('q') == -1]:
                for r in ((0, 1), (1,))[logic.find('r') == -1]:
                    for s in ((0, 1), (1,))[logic.find('s') == -1]:
                        for t in ((0, 1), (1,))[logic.find('t') == -1]:
                            stack = []
                            for i in logic:
                                if i in 'KANCE':
                                    stack.append(i)
                                else:
                                    stack.append(eval(i))
                            stack2 = []
                            while stack not in ([0], [1]):
                                stack2.append(stack.pop())
                                if stack2[-1] in list('KANCE'):
                                    op = stack2.pop()
                                    if op == 'N':
                                        stack.append(1 - stack2.pop())
                                    elif op == 'A':
                                        stack.append(stack2.pop() | stack2.pop())
                                    elif op == 'K':
                                        stack.append(stack2.pop() & stack2.pop())
                                    elif op == 'C':
                                        stack.append((1 - stack2.pop()) | stack2.pop())
                                    else:
                                        stack.append(1 - (stack2.pop() ^ stack2.pop()))
                            if not stack[-1]:
                                return False
        return True

    print('tautology' if check() else 'not')