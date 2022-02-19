n = int(input())
for _ in range(n):
    s = input().split(',')
    r = 0
    for i in s:
        r *= 60
        if i != '':
            r += int(i)
    print(r)