def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
    
def lcm(a,b):
    return a*b//gcd(a,b)
    
n = int(input())
for _ in range(n):
    input()
    p = list(map(int, input().split()))
    ans = 1
    for i in p:
        ans = lcm(ans, i)
    if ans > 10**9:
        print('More than a billion.')
    else:
        print(ans)