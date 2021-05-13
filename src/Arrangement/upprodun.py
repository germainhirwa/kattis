n = int(input())
m = int(input())

arr = '*'*m
for i in range(n):
    print(arr[int(i*m/n):int((i+1)*m/n)])