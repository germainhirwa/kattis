q, m, s, l = map(int, input().split())
offset = l//m*q; l %= m; h = 1
while (s+h-1)//h>m-l: h += 1
print(max(h*(s>0), q*(l>0))+offset)