n = int(input())
s = [1]
while s[-1] <= n//2: s.append(s[-1]*2)
print(len(s)), print(*s)