for _ in range(int(input())):
    t, x, y = map(int, input().split())
    if x < y: print(t, 2, x, y)
    elif x > 2 and y > 2: print(t, 6, 1, 2, 3, x-y+5, x+2, x+3)
    else: print(t, 'NO PATH')