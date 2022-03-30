import sys

for line in sys.stdin:
    cnt = 0
    curr = line[0]
    for i in line.strip():
        if i == curr:
            cnt += 1
        else:
            print(f'{cnt}{curr}', end='')
            curr, cnt = i, 1
    print(f'{cnt}{curr}')