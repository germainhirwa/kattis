n = int(input())

def choose(n, m):
    if n <= 0 or m < 0:
        return 0
    if n == m or m == 0:
        return 1 # not necessary but is fine
    result = 1
    for i in range(m):
        result *= (n-i)/(i+1)
    return int(result)

for _ in range(n):
    r, s, x, y, w = list(map(int, input().split()))
    p = 0
    for i in range(x, y + 1):
        p += choose(y, i) * ((s-r+1)/s)**(i) * (1-(s-r+1)/s)**(y-i)
    print(["no", "yes"][int((w-1)*p > (1-p))])