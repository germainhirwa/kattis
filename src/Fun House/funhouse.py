c = 1
while True:
    l, w = map(int, input().split())
    if w == l == 0:
        break

    house = []
    er, ec = None, None
    for i in range(w):
        t = input()
        if t.find('*') != -1:
            er, ec = i, t.find('*')
        house.append(list(t))

    if er == 0:
        dr, dc = 1, 0
    elif er == w - 1:
        dr, dc = -1, 0
    elif ec == 0:
        dr, dc = 0, 1
    else:
        dr, dc = 0, -1
    
    while True:
        er += dr
        ec += dc
        if not (1 <= er <= w - 2 and 1 <= ec <= l - 2):
            break
        if house[er][ec] == '/':
            dr, dc = -dc, -dr
        elif house[er][ec] == '\\':
            dr, dc = dc, dr
    house[er][ec] = '&'

    print('HOUSE', c)
    for r in house:
        print(''.join(r))
    c += 1