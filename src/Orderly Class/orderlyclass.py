s1, s2 = input(), input()
ptr = 0
while ptr < len(s1) and s1[ptr] == s2[ptr]:
    ptr += 1
ptr2 = len(s1) - 1
while ptr2 >= ptr and s1[ptr2] == s2[ptr2]:
    ptr2 -= 1
ptr2 += 1

ans = int(s1[ptr:ptr2] == s2[ptr:ptr2][::-1])
if s1[ptr] == s2[ptr2 - 1] and ans:
    while ptr >= 1 and ptr2 < len(s1) and s1[ptr - 1] == s2[ptr2]:
        ptr -= 1
        ptr2 += 1
        ans += 1
print(ans)