n,t = list(map(int,input().split(" ")))
s = list(map(int,input().split(" ")))

c = 0
while t >= 0 and c < n:
    t -= s[c]
    if t >= 0:
        c += 1
print(c)