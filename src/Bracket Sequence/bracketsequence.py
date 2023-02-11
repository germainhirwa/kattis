n = int(input())
tokens = input().strip().split()
s1, s2, d = [], [], 0

MOD = 10**9+7

op = [lambda x,y: (x+y)%MOD, lambda x,y: (x*y)%MOD]
for token in tokens:
    if token == '(':
        d += 1
        s1.append(token)
    elif token == ')':
        while s1[-1] != '(': s2.append(s1.pop())
        s1.pop()
        s = d%2
        while s2: s = op[d%2](s, s2.pop())
        s1.append(s)
        d -= 1
    else:
        s1.append(int(token))
print(sum(s1) % MOD)