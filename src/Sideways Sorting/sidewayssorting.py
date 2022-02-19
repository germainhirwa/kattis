while True:
    r, c  = list(map(int, input().split()))
    if [r, c] == [0, 0]:
        break

    arr = []
    for _ in range(r):
        arr.append(list(input()))
    arr = list(map(list, zip(*arr)))
    arr.sort(key=lambda x: list(map(lambda y: y.lower(), x)))
    arr = list(map(list, zip(*arr)))
    for r in arr:
        print(''.join(r))
    print()