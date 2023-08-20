dpg = [*map(int, input().strip().split('+'))]; vals = set()
dig = [len(str(i)) for i in dpg]
for i in range(1<<(len(dpg)-1)):
    v = [dpg[0]]
    for j in range(len(dpg)-1):
        if (i&(1<<j)): v[-1] *= 10**dig[j+1]; v[-1] += dpg[j+1]
        else: v.append(dpg[j+1])
    vals.add(sum(v))
print(len(vals))