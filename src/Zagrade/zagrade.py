bs = [*input().strip()]
ans = set()
b = []; op = []
for i in range(len(bs)):
    if bs[i] == '(': op.append(i)
    elif bs[i] == ')': b.append((op.pop(), i))

for bm in range(1, 1<<len(b)):
    s = []
    for i in range(len(b)):
        if bm&(1<<i): s.append(b[i])
    for i in s: bs[i[0]] = bs[i[1]] = ''
    ans.add(''.join(bs))
    for i in s: bs[i[0]] = '('; bs[i[1]] = ')'
for i in sorted(ans): print(i)