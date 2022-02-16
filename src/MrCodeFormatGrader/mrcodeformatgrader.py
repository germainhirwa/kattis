c, n = list(map(int, input().split()))
arr = list(map(int, input().split()))
errs, ok = [], []

cp = 0
pos = 1
while cp < n:
    while pos < n and arr[pos] - 1 == arr[pos - 1]:
        pos += 1
    errs.append([arr[cp], arr[pos - 1]])
    cp, pos = pos, pos + 1

if errs[0][0] != 1:
    ok.append([1, errs[0][0] - 1])
for i in range(1, len(errs)):
    ok.append([errs[i - 1][1] + 1, errs[i][0] - 1])
if errs[-1][-1] != c:
    ok.append([errs[-1][-1] + 1, c])

print('Errors: ', end='')
for err in errs[:-2]:
    if err[0] == err[1]:
        print(err[0], end=', ')
    else:
        print(f'{err[0]}-{err[1]}', end=', ')
if len(errs) >= 2:
    err = errs[-2]
    if err[0] == err[1]:
        print(err[0], end=' and ')
    else:
        print(f'{err[0]}-{err[1]}', end=' and ')
err = errs[-1]
if err[0] == err[1]:
    print(err[0])
else:
    print(f'{err[0]}-{err[1]}')

print('Correct: ', end='')
for cor in ok[:-2]:
    if cor[0] == cor[1]:
        print(cor[0], end=', ')
    else:
        print(f'{cor[0]}-{cor[1]}', end=', ')
if len(ok) >= 2:
    cor = ok[-2]
    if cor[0] == cor[1]:
        print(cor[0], end=' and ')
    else:
        print(f'{cor[0]}-{cor[1]}', end=' and ')
cor = ok[-1]
if cor[0] == cor[1]:
    print(cor[0])
else:
    print(f'{cor[0]}-{cor[1]}')