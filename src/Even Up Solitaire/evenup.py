n, arr = int(input()), list(map(int, input().split()))
while True:
    s, c = [], 0
    for i in arr:
        if not s or (s[-1] + i) % 2:    s.append(i)
        else:                           c = [1, s.pop()][0]
    if not c:
        print(len(s))
        break
    arr = s