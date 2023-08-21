n, r, k = map(int, input().split())
print(max(n, k+abs(r-k))+r+((n-r)%2 and n>k+abs(r-k)))