ans = 0
index = 0
for i in range(5):
    s = list(map(int,input().split(" ")))
    if sum(s) > ans:
        ans = sum(s)
        index = i+1

print(index,ans)