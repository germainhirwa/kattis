kunas = list(map(int,input().split()))
a1, a2 = list(map(int,input().split()))
b1, b2 = list(map(int,input().split()))
c1, c2 = list(map(int,input().split()))

p = 0
for i in range(min(a1,b1,c1),max(a2,b2,c2)):
    trucks = int(i in range(a1,a2)) + int(i in range(b1,b2)) + int(i in range(c1,c2))
    p += trucks*kunas[trucks-1]
print(p)