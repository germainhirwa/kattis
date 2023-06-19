t, s = map(int, input().split())
ss = sorted(map(int, input().split()))
a = 0
for i in ss:
    if a+i < 60*t: a += i
print(a)