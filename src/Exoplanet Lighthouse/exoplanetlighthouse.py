from math import *
for _ in range(int(input())):
    r, h1, h2 = map(float, input().split())
    print(r*(acos(r/(r+h1/1000))+acos(r/(r+h2/1000))))