t = int(input()); s = [*enumerate(map(int, input().split()))]; a = 0
for _ in range(t-1): a %= len(s); a = (a+s[a][1]-1)%len(s); s.pop(a)
print(s[0][0]+1)