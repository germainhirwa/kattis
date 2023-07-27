import sys
for l in sys.stdin:
    if l[0] == 'E': break
    l = l.strip()
    it = 1
    while True:
        if (x:=str(len(l))) == l: break
        l = x; it += 1
    print(it)