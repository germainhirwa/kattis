l, r = list(map(int, input().split()))
print(['nope', 'fits'][2 * r**2 > l**2])