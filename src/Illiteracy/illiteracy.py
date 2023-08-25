from collections import deque
s, t = [*map(lambda x: ord(x)-65, input().strip())], [*map(lambda x: ord(x)-65, input().strip())]
q = deque([(int(''.join(map(str, s))), 0)]); vis = set(); t = int(''.join(map(str, t)))
while q:
    u, d = q.popleft()
    if u == t: print(d); break
    if u in vis: continue
    vis.add(u)
    for i in range(8):
        b = [*map(int, str(u).zfill(8))]
        if b[i] == 0:
            if i > 0: b[i-1] = (b[i-1]+1)%6
            if i < 7: b[i+1] = (b[i+1]+1)%6
        elif b[i] == 1:
            if i*(i-7): b[i+1] = b[i-1]
        elif b[i] == 2:
            b[7-i] = (b[7-i]+1)%6
        elif b[i] == 3:
            if i < 4:
                for j in range(i): b[j] = (b[j]+1)%6
            else:
                for j in range(i+1, 8): b[j] = (b[j]+1)%6
        elif b[i] == 4:
            if i*(i-7):
                if i < 4:
                    b[0] = (b[0]+1)%6
                    b[2*i] = (b[2*i]+1)%6
                else:
                    b[7] = (b[7]+1)%6
                    b[2*i-7] = (b[2*i-7]+1)%6
        else:
            if i%2: b[(i-1)//2] = (b[(i-1)//2]+1)%6
            else: b[i//2+4] = (b[i//2+4]+1)%6
        q.append((int(''.join(map(str, b))), d+1))