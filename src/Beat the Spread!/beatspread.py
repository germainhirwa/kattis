for _ in range(int(input())):
    s, d = map(int, input().split())
    if s < d or (s+d)%2: print('impossible')
    else: print((s+d)//2, (s-d)//2)