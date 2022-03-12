r, c, f, s, g = map(int, input().split())
facs = []
stus = []
for _ in range(f):
    temp = list(map(int, input().split()))
    k = temp[0]
    facs.append([])
    stus.append([])
    for i in range(k):
        facs[-1].append([temp[2*i+1], temp[2*i+2]])
for _ in range(s):
    rr, cc, sn, ff = map(int, input().split())
    stus[ff - 1].append([sn, rr, cc])
ts = list(map(int, input().split()))

md = []
facs = list(map(sorted, facs))
stus = list(map(sorted, stus))

for i in range(f):
    d = []
    for j in range(len(stus[i])):
        _, rx, cx = stus[i][j]
        rxx, cxx = facs[i][j]
        d.append(abs(rx - rxx) + abs(cx - cxx))
    md.append(sum(sorted(d)[:ts[i]]))
print(sum(sorted(md)[:g]))