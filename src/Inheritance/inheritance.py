p = int(input())
can = set()
s = [0]
while s:
    u = s.pop()
    if u > p: continue
    can.add(u)
    s.append(10*u+2), s.append(10*u+4)
for i in sorted(can)[1:]:
    if p % i == 0: print(i)
    if i > p: break