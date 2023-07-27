import sys
C = [l.strip() for l in sys.stdin]
MM = []
def bt(c, i=0, b=[0]*9, s=511):
    # every 3x3 has 12 constraints
    '''
    . > . > .   --> c[0], c[1]
    =   =   =   --> c[2], c[3], c[4]
    . > . > .   --> c[5], c[6]
    =   =   =   --> c[7], c[8], c[9]
    . > . > .   --> c[10], c[11]
    '''
    if i == 9:
        t = 0
        for i in b: t *= 10; t += i
        M.append(str(t))
    elif i == 0:
        for v in range(1, 10):
            b[0] = v; bt(c, 1, b, s-(1<<(v-1)))
    elif i < 3:
        if c[i-1] == '>':
            for j in range(11, b[i-1]+10):
                k = j-b[i-1]
                if s&(1<<(k-1)): b[i] = k; bt(c, i+1, b, s-(1<<(k-1)))
        elif c[i-1] == '<':
            for j in range(1, 10-b[i-1]):
                if s&(1<<(j-1)): b[i] = j; bt(c, i+1, b, s-(1<<(j-1)))
        elif b[i-1] != 5 and s&(1<<(9-b[i-1])):
            b[i] = 10-b[i-1]; bt(c, i+1, b, s-(1<<(b[i]-1)))
    elif i == 3 or i == 6:
        t = 5*i//3-3
        if c[t] == '>':
            for j in range(11, b[i-3]+10):
                k = j-b[i-3]
                if s&(1<<(k-1)): b[i] = k; bt(c, i+1, b, s-(1<<(k-1)))
        elif c[t] == '<':
            for j in range(1, 10-b[i-3]):
                if s&(1<<(j-1)): b[i] = j; bt(c, i+1, b, s-(1<<(j-1)))
        elif b[i-3] != 5 and s&(1<<(9-b[i-3])):
            b[i] = 10-b[i-3]; bt(c, i+1, b, s-(1<<(b[i]-1)))
    else:
        up = i+i//3*2-3; left = up+2
        if c[up] == '=' and b[i-3] != 5 and s&(1<<(9-b[i-3])):
            b[i] = 10-b[i-3]; bt(c, i+1, b, s-(1<<(b[i]-1)))
        elif c[left] == '=' and b[i-1] != 5 and s&(1<<(9-b[i-1])):
            b[i] = 10-b[i-1]; bt(c, i+1, b, s-(1<<(b[i]-1)))
        elif c[up] != '=' and c[left] != '=':
            if c[up] == '>' and c[left] == '>':
                for j in range(11, min(b[i-3], b[i-1])+10):
                    k = j-min(b[i-3], b[i-1])
                    if s&(1<<(k-1)): b[i] = k; bt(c, i+1, b, s-(1<<(k-1)))
            elif c[up] == '<' and c[left] == '<':
                for j in range(1, 10-max(b[i-3], b[i-1])):
                    if s&(1<<(j-1)): b[i] = j; bt(c, i+1, b, s-(1<<(j-1)))
            elif c[up] == '<' and c[left] == '>':
                for j in range(1, 10):
                    if s&(1<<(j-1)) and b[i-3]+j<10 and b[i-1]+j>10: b[i] = j; bt(c, i+1, b, s-(1<<(j-1)))
            else:
                for j in range(1, 10):
                    if s&(1<<(j-1)) and b[i-3]+j>10 and b[i-1]+j<10: b[i] = j; bt(c, i+1, b, s-(1<<(j-1)))

for i in range(3):
    for j in range(3):
        M = []; bt(C[5*i][2*j:2*j+2]+C[5*i+1][3*j:3*j+3]+C[5*i+2][2*j:2*j+2]+C[5*i+3][3*j:3*j+3]+C[5*i+4][2*j:2*j+2]); MM.append(M)

from copy import deepcopy
def fill(idx=0, b=[['']*9 for _ in range(9)], bm=[511]*18):
    if idx == 9:
        for r in b: print(' '.join(r))
        exit(0)
    def util(sb):
        t = 0; b2 = deepcopy(b); bm2 = bm.copy()
        for i in range(3*(idx//3), 3*(idx//3+1)):
            for j in range(3*(idx%3), 3*(idx%3+1)):
                e = 1<<(int(sb[t])-1)
                if bm2[i]&e == 0: return
                if bm2[9+j]&e == 0: return
                b2[i][j] = sb[t]; t += 1; bm2[i] -= e; bm2[9+j] -= e
        fill(idx+1, b2, bm2)
    for sb in MM[idx]: util(sb)
fill()
assert False