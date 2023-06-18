n, m = map(int, input().split())
s = {int(input()) for _ in range(m)}
for i in range(n):
    if i not in s: print(i)
print(f'Mario got {len(s)} of the dangerous obstacles.')