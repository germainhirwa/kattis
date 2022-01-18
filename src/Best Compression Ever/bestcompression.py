N, b = list(map(int, input().split()))
print(['no', 'yes'][int(N <= 2**(b + 1) - 1)])