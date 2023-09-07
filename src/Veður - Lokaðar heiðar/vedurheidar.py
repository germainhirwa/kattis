v = int(input()); n = int(input())
for _ in range(n): r, k = input().split(); print(r, ['opin', 'lokud'][int(k) < v])