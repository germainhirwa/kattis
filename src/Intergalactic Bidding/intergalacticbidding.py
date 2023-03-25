def conv(_):
    a, b = input().split()
    return a, int(b)

n, s = map(int, input().split())
bids = sorted(map(conv, range(n)), key=lambda x: -x[1])
win, c = [], 0
for p, b in bids:
    if c+b <= s:
        win.append(p)
        c += b
if c != s: print(0)
else:
    print(len(win))
    for i in win: print(i)