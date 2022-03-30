import sys

s = input()
n = len(s)
for k in range(1, n):
    if n % k == 0:
        temp = s[:k]
        ok = True
        for i in range(1, n // k):
            if temp[-1] + temp[:-1] == s[k*i:k*(i+1)]:
                temp = temp[-1] + temp[:-1]
            else:
                ok = False
                break
        if ok:
            print(k)
            sys.exit(0)
print(n)