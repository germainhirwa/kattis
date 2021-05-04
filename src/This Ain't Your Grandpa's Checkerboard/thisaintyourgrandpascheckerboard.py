import sys

gr = []

for line in sys.stdin:
    try:
        k = int(line)
    except:
        gr.append(list(line.strip()))

grt = [[gr[i][j] for i in range(k)] for j in range(k)]

check = True
for i in range(k):
    if gr[i].count('W') != k//2 or grt[i].count('W') != k//2 or'WWW' in ''.join(gr[i]) or 'WWW' in ''.join(grt[i]) or 'BBB' in ''.join(gr[i]) or 'BBB' in ''.join(grt[i]):
        check = False
print(int(check))