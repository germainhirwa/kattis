rev = {e:i for i,e in enumerate(input().split())}
s = [input().split() for _ in range(int(input()))]
for _ in range(int(input())):
    c = rev[input()]; print(' '.join(rev))
    s.sort(key=lambda x: x[c])
    for i in s: print(' '.join(i))
    print()