while True:
    n = int(input())
    if n == 0:
        break
    a,a2,b = [],[],[]
    ad,bd = {},{}
    for _ in range(n):
        k = int(input())
        a.append(k)
        a2.append(k)
    for _ in range(n):
        b.append(int(input()))
    a.sort()
    b.sort()
    for i in range(n):
        ad[a[i]] = i
        bd[i] = b[i]
    for i in range(n):
        print(bd[ad[a2[i]]])
    print()