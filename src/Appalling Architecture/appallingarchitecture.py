r, c = map(int, input().split())
pts = []
ft = []
for i in range(r):
    s = input()
    for j in range(c):
        if s[j] != '.':
            pts.append(j)
            if i == r-1: ft.append(j)
l, r, x = ft[0], ft[-1], sum(pts)/len(pts)
if l-0.5<=x<=r+0.5: print('balanced')
elif x<l-0.5: print('left')
else: print('right')