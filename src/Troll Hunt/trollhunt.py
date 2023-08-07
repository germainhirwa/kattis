from math import ceil
b, k, g = map(int, input().split())
print(ceil((b-1)/(k//g)))