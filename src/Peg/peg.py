m = []
for _ in range(7):
    m.append(list(input()))
    
ans = 0
for i in range(7):
    for j in range(7):
        if i >= 2 and m[i][j] == 'o' and m[i - 1][j] == 'o' and m[i - 2][j] == '.':
            ans += 1
        if i <= 4 and m[i][j] == 'o' and m[i + 1][j] == 'o' and m[i + 2][j] == '.':
            ans += 1
        if j >= 2 and m[i][j] == 'o' and m[i][j - 1] == 'o' and m[i][j - 2] == '.':
            ans += 1
        if j <= 4 and m[i][j] == 'o' and m[i][j + 1] == 'o' and m[i][j + 2] == '.':
            ans += 1
print(ans)