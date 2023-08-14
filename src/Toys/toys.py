t, k = map(int, input().split()); a = 0
for i in range(t): a = (a+k)%(i+1)
print(a)