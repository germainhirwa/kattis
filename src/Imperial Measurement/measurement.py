v, u, i, ut = input().strip().split(" ")
v = int(v)

d = {}
k = 1
scales = [1, 1000, 12, 3, 22, 10, 8, 3]
names = ["thou", "inch", "foot", "yard", "chain", "furlong", "mile", "league"]
acronyms = ["th", "in", "ft", "yd", "ch", "fur", "mi", "lea"]
for p in range(8):
    k *= scales[p]
    d[names[p]] = k
    d[acronyms[p]] = k
    
print(d[u]/d[ut]*v)