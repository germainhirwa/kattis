n = int(input())
q = []
for _ in range(n):
    q.append(input())

m = int(input())
for _ in range(m):
    cmd = input().split()
    if cmd[0] == 'cut':
        q.insert(q.index(cmd[2]), cmd[1])
    else:
        q.remove(cmd[1])

for p in q:
    print(p)