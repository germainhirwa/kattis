n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(sum(map(lambda i: len([x for x in arr[i:i+m] if x%2==0]) >= 2, range(n-m+1))))