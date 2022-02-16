from collections import deque

n, m, c = list(map(int, input().split()))
arr = list(map(int, input().split()))

dqmin = deque()
dqmax = deque()
dq = deque()

found = False
for i in range(n):
    curr = arr[i]
    while dqmin and dqmin[-1] > curr:
        dqmin.pop()
    while dqmax and dqmax[-1] < curr:
        dqmax.pop()
    dqmin.append(curr)
    dqmax.append(curr)
    dq.append(curr)

    if i >= m:
        x = dq.popleft()
        if x == dqmax[0]:
            dqmax.popleft()
        if x == dqmin[0]:
            dqmin.popleft()
    if i >= m - 1 and dqmax[0] - dqmin[0] <= c:
        found = True
        print(i - m + 2)
if not found:   print('NONE')