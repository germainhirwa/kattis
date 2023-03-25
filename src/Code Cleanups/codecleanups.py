c, d, dd, r = 0, [input(), list(map(int, input().split()))][1][::-1], 0, 0
for i in range(1, 366):
    if not d: break
    if i == d[-1]: r += 1; d.pop()
    if dd + r >= 20:    dd, r, c = 0, 0, c + 1
    else:               dd += r
print(c+(dd!=0))