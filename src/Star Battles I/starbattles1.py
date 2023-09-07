r = [[*map(int, input().strip())] for _ in range(10)]
s = [input() for _ in range(10)]
c1, c2, c3 = [0]*10, [0]*10, [0]*10
for i in range(10):
    for j in range(10):
        if s[i][j] == '*': c1[r[i][j]] += 1; c2[i] += 1; c3[j] += 1
for i in range(10):
    for j in range(10):
        if (j < 9 and s[i][j] == s[i][j+1] == '*') or (i < 9 and s[i][j] == s[i+1][j] == '*') or (i < 9 and j < 9 and (s[i+1][j] == s[i][j+1] == '*' or s[i][j] == s[i+1][j+1] == '*')): print('invalid'), exit(0)
print('valid' if c1==c2==c3==[2]*10 else 'invalid')