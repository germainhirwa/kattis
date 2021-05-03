a,b,c = list(map(int,input().split(" ")))
d = sorted([a,b,c])
aa,bb,cc = d

if aa + cc == 2*bb:
    print(bb+cc-aa)
elif bb-aa == 2*(cc-bb):
    print((aa+bb)//2)
elif cc-bb == 2*(bb-aa):
    print((bb+cc)//2)