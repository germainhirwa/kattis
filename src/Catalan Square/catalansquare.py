import sys

c = [1]*5000
for i in range(1,5000):
    c[i] = c[i-1]*(4*i+2)
    c[i] //= (i+2)
c.insert(0, 1)

s = int(input())
ans = 0
for i in range(s + 1):
    ans += c[i] * c[s - i]
print(ans)