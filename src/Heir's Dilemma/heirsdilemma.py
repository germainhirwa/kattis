def possible(n):
    def helper(x,y):
        if y == 0:
            return True
        elif y % 10 != 0 and x % (y%10) == 0:
            return helper(x,y//10)
        else:
            return False
    return helper(n,n)

def distinct(n):
    s = str(n)
    d = {}
    for v in s:
        d[v] = d.get(v,0)+1
    return len(s) == len(d)

a,b = list(map(int,input().split()))
c = 0
for i in range(a,b+1):
    if distinct(i):
        c += int(possible(i))

print(c)