s1, s2 = input(), input()
ans = 1
for i in range(4):
    if s1[i] != s2[i]:
        ans *= 2
print(ans)