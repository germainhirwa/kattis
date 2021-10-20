p, t = list(map(int, input().split()))
ans = 0

for _ in range(p):
    solved = True
    for _ in range(t):
        s = input()
        if s.lower() != s:
            if s.lower() != s[0].lower() + s[1:]:
                solved = False
            
    ans += int(solved)
    
print(ans)