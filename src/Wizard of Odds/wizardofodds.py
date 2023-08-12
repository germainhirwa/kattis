n, k = map(int, input().split())
print(['You will become a flying monkey!', 'Your wish is granted!'][k>350 or 2**k>=n])