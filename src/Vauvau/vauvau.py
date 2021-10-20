a,b,c,d = list(map(int,input().split()))
lst = list(map(int,input().split()))

for e in lst:
    count = int(0 < e % (a+b) <= a) + int(0 < e % (c+d) <= c)
    print(["none","one","both"][count])