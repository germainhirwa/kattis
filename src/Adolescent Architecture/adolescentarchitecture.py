s = []
for _ in range(int(input())):
    t, r = input().split(); r = int(r)
    if t == 'cube': s.append([t, r, r, r**2])
    else: s.append([t, r, 2*r, 2*r**2])
s.sort(key=lambda x: (x[2], x[3]))
for i in range(len(s)-1):
    if s[i][0] == 'cube' and s[i+1][0] == 'cylinder' and s[i][3] > s[i+1][3]: print('impossible'), exit(0)
for t, r, *_ in s: print(t, r)