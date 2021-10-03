n = -1
while n != 0:
    n = int(input())
    if n == 0:
        break

    s = input()
    p = input()
    c = input()

    d = int(len(c)**1.5 + n) % len(c)
    m = [""]*len(c)
    m[d] = p[s.index(c[d])]
    for i in range(1, len(c)):
        i = (d - i) % len(c) # m[(i+1) % len(c)] exists!
        m[i] = p[s.index(m[(i+1) % len(c)])^s.index(c[i])]
    print(str().join(m))