kb = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
qf = {}
for i in range(3):
    for j in kb[i]:
        qf[j] = i
        
t = int(input())
for _ in range(t):
    w, k = input().split()
    p = []
    for _ in range(int(k)):
        s = 0
        c = input()
        for i in range(len(c)):
            s += abs(qf[c[i]] - qf[w[i]]) + abs(kb[qf[c[i]]].find(c[i]) - kb[qf[w[i]]].find(w[i]))
        p.append((c, s))
    p.sort(key=lambda x: x[::-1])
    for r in p:
        print(*r)