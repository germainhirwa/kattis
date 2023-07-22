import string
import sys; input = sys.stdin.readline

def mul(a, b):
    c = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])): c[i][j] = sum(a[i][k]*b[k][j] for k in range(len(a[0]))) % 37
    return c

rt = dict(enumerate(string.ascii_uppercase+'0123456789 '))
tr = {e:i for i,e in rt.items()}
n = int(input())
mat = [[*map(int, input().split())] for _ in range(n)]
s = input().strip()
ss = [tr[i] for i in s]
while len(ss) % n: ss.append(36)
cut = [[[j] for j in ss[n*i:n*i+n]] for i in range(len(ss)//n)]
cutmul = [[j[0] for j in i] for i in [mul(mat, i) for i in cut]]
res = []
for i in cutmul: res.extend(i)
print(''.join(map(lambda x: rt[x], res)))