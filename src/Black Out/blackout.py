for _ in range(int(input())):
    print('3 1 3 6')
    while True:
        cmd = input().split()
        if cmd[0] == 'GAME': break
        else:
            r1, c1, r2, c2 = map(int, cmd[1:])
            print(6-max(r1,r2), 7-max(c1,c2), 6-min(r1,r2), 7-min(c1,c2))