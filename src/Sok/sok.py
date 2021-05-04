a,b,c = list(map(int,input().split(" ")))
i,j,k = list(map(int,input().split(" ")))
m = min(a/i,b/j,c/k)
print(a-m*i,b-m*j,c-m*k)