a, b, c = map(int, input().split())
v1, v2 = b - a, c - b
if v1/abs(v1) != v2/abs(v2):
    print('turned')
elif abs(v2) > abs(v1):
    print('accelerated')
elif abs(v2) < abs(v1):
    print('braked')
else:
    print('cruised')