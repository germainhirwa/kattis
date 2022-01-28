l, h, g = int(input()), 0, 0

while l:
    m, n, k = list(map(int, input().split()))
    b = []
    for _ in range(n):
        b.append(input())
    
    def check():
        t = b[::-1]

        # check Hansel = x
        for row in b:
            if row.find('x' * k) != -1:
                return [1, 0]
        for i in range(m):
            if ''.join(list(map(lambda x: x[i], b))).find('x' * k) != -1:
                return [1, 0]
        for xpy in range(n + m - 1):
            d = []
            for i in range(n):
                j = xpy - i
                if j in range(m):
                    d.append(b[i][j])
            if ''.join(d).find('x' * k) != -1:
                return [1, 0]
        for xpy in range(n + m - 1):
            d = []
            for i in range(n):
                j = xpy - i
                if j in range(m):
                    d.append(t[i][j])
            if ''.join(d).find('x' * k) != -1:
                return [1, 0]
        
        # check Gretel = o
        for row in b:
            if row.find('o' * k) != -1:
                return [0, 1]
        for i in range(m):
            if ''.join(list(map(lambda x: x[i], b))).find('o' * k) != -1:
                return [0, 1]
        for xpy in range(n + m - 1):
            d = []
            for i in range(n):
                j = xpy - i
                if j in range(m):
                    d.append(b[i][j])
            if ''.join(d).find('o' * k) != -1:
                return [0, 1]
        for xpy in range(n + m - 1):
            d = []
            for i in range(n):
                j = xpy - i
                if j in range(m):
                    d.append(t[i][j])
            if ''.join(d).find('o' * k) != -1:
                return [0, 1]
        
        return [0, 0]
    
    dh, dg = check()
    h += dh
    g += dg
    l -= 1
print(f'{h}:{g}')