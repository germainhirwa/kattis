for _ in range(int(input())):
    c, p = 0, []
    for _ in range(int(input())): p.append(input())
    p.sort()
    for i in range(len(p)-1):
        if p[i] == p[i+1][:len(p[i])]:
            c = 1
            break
    print('YNEOS'[c::2])