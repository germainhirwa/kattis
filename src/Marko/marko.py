t9 = {}
for c in range(97, ord('s')):
    t9[chr(c)] = (c - 91) // 3
for c in range(ord('t'), ord('z')):
    t9[chr(c)] = (c - 92) // 3
t9['s'], t9['z'] = 7, 9

n = int(input())
txt = []
for _ in range(n):
    txt.append(input())
s = input()
print(len(list(filter(lambda x: s == ''.join(list(map(lambda y: str(t9[y]), x))), txt))))