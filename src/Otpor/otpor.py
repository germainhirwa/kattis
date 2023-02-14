n = int(input())
rr = list(map(float, input().split()))
s1, s2 = [], []
for token in input().strip().replace('R', ''):
    if token != ')':
        s1.append(token)
    else:
        while s1[-1] != '(':
            s2.append(s1.pop())
        s1.pop()
        am, hm, use = 0, 0, None
        while s2:
            p = s2.pop()
            if type(p) != str:
                am += p
                hm += 1/p
            elif p.isdigit():
                p = int(p)
                am += rr[p-1]
                hm += 1/rr[p-1]
            elif p == '|':  use = 0
            elif p == '-':  use = 1
        s1.append([1/hm, am][use])
print(s1[0])