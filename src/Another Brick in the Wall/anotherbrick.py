h, w, n = list(map(int, input().split()))
x = list(map(int, input().split()))

can = True
c, r = 0, 1
for i in range(n):
    if c <= w - x[i]:
        c += x[i]
    elif c != w:
        can = False
        break
    else:
        if r == h:
            break
        r += 1
        c = 0
        if c <= w - x[i]:
            c += x[i]
        elif c != w:
            can = False
            break

print(["NO", "YES"][int(can)])