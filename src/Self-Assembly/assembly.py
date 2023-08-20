n = int(input()); rev = {}
for i in range(26): rev[chr(i+65)+'+'] = len(rev); rev[chr(i+65)+'-'] = len(rev)
rev['00'] = 52
D = [[0]*52 for _ in range(52)]
for m in input().strip().split():
    tup = (rev[m[:2]], rev[m[2:4]], rev[m[4:6]], rev[m[6:]])
    for i in range(4):
        for j in range(4):
            if tup[i] == 52 or tup[j] == 52: continue
            if i != j: D[tup[i]][tup[j]^1] = 1
for k in range(52):
    for i in range(52):
        for j in range(52): D[i][j] |= D[i][k]&D[k][j]
print('un'*any(D[i][i] for i in range(52))+'bounded')