t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    bits = []
    for _ in range(r):
        bits.append(input())
    d = {}
    for i in range(r):
        for j in range(c):
            if j not in d:
                d[j] = [0, 0]
            d[j][int(bits[i][j])] += 1
    
    def sin(bit):
        s = 0
        for i in range(len(bit)):
            s += d[i][int(bit[i])]
        return s

    for i in range(c):
        if d[i][0] >= d[i][1]:
            print(0, end='')
        else:
            print(1, end='')
    print()