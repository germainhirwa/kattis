def win(a, b):
    if a < b: a, b = b, a
    if a % b == 0: return 1
    if 2*b > a > b: return 1-win(a-b, b)
    return 1
a, b = map(int, input().split())
print(['lose', 'win'][win(a, b)])