import sys
input()

chat, f = {}, {}
for line in sys.stdin:
    line = line.strip().split()
    if line[0] not in chat:
        chat[line[0]] = set()
    
    for r in line[1:]:
        chat[line[0]].add(r)
        if r not in f:
            f[r] = 0
        f[r] += 1

words = []
freq = {}
for v in chat.values():
    ww = set()
    for w in v:
        if w not in freq:
            freq[w] = 0
        if w not in ww:
            freq[w] += 1
            ww.add(w)

for k in freq:
    if freq[k] == len(chat):
        words.append(k)
        
words.sort(key=lambda x: (-f[x], x))
for i in words:
    print(i)
    
if not words:
    print('ALL CLEAR')