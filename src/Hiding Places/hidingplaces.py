import sys

def gindex(pos):
    return "abcdefgh"[::-1].find(pos[0]) + (int(pos[1]) - 1)*8
    
def indexg(num):
    return "abcdefgh"[::-1][num % 8] + str(num // 8 + 1)
    
def rtc(r, c):
    return 8*r + c
    
def neighbours(r, c):
    res = []
    for dr in range(-2, 3):
        for dc in range(-2, 3):
            if abs(dr) + abs(dc) == 3 and (r + dr) in range(8) and (c + dc) in range(8):
                res.append(rtc(r + dr, c + dc))
    return res
    
def BFS(num):
    al = {}
    for i in range(8):
        for j in range(8):
            al[rtc(i, j)] = neighbours(i, j)
            
    visited = [0]*64
    visited[num] = 1
    q = [num]
    while q:
        u = q.pop(0)
        for v in al[u]:
            if not visited[v]:
                visited[v] = visited[u] + 1
                q.append(v)
    
    d = max(visited)
    res = [str(d-1)]
    for i in range(64):
        if visited[i] == d:
            res.append(indexg(i))
    return [res[0]] + res[1:][::-1]

fl = True
for line in sys.stdin:
    if fl:
        fl = False
    else:
        print(' '.join(BFS(gindex(line))))