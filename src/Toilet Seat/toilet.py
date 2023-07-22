t = input()
u = d = f = 0
s = t[0]
for i in range(1, len(t)):
    if t[i] != s: u += 1; s = t[i]
    if s != 'U': u += 1; s = 'U'
s = t[0]
for i in range(1, len(t)):
    if t[i] != s: d += 1; s = t[i]
    if s != 'D': d += 1; s = 'D'
s = t[0]
for i in range(1, len(t)):
    if t[i] != s: f += 1; s = t[i]
print(u, d, f)