_, arr = input(), list(map(int, input().split()))
s = sum(arr)
t = {s-i for i in arr}
print(len(t))
print(*sorted(t))