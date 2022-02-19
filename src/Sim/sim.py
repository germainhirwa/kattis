from collections import deque

t = int(input())
for _ in range(t):
    s = input()
    big = deque([])
    back = True
    q = []
    for c in s:
        if c == '<':
            if q:
                q.pop()
            elif big and back:
                while big and not big[-1]:
                    big.pop()
                if big:
                    big[-1].pop()
        elif c in '[]':
            if back:    big.append(q)
            else:       big.appendleft(q)
            q, back = [], c == ']'
        else:
            q.append(c)
    if q:
        if back:    big.append(q)
        else:       big.appendleft(q)
    final = []
    for b in big:
        final.extend(b)
    print(''.join(final))