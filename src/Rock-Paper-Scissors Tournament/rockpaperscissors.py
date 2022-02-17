fl = True
while True:
    line = input()
    if line == '0':
        break

    if not fl:
        print()
    fl = False

    n, k = list(map(int, line.split()))
    win = [0] * n
    wpl = [0] * n
    for _ in range(k * n * (n-1) // 2):
        p1, m1, p2, m2 = input().split()
        p1, p2 = int(p1) - 1, int(p2) - 1

        for _ in range(2):
            p1, m1, p2, m2 = p2, m2, p1, m1
            if m1 == 'rock' and m2 == 'scissors':
                win[p1] += 1
                wpl[p1] += 1
                wpl[p2] += 1
            if m1 == 'scissors' and m2 == 'paper':
                win[p1] += 1
                wpl[p1] += 1
                wpl[p2] += 1
            if m1 == 'paper' and m2 == 'rock':
                win[p1] += 1
                wpl[p1] += 1
                wpl[p2] += 1

    for i in range(n):
        if wpl[i] == 0:
            print('-')
        else:
            print('%.3f'%(win[i] / wpl[i]))