n = int(input())
y = input()
f = input()
q = len(y)

match = sum(int(y[x] == f[x]) for x in range(q))
mismatch = q - match
xors = q - n
print(min(match, n) + min(mismatch, xors))