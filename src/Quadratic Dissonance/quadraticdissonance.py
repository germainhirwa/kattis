A, B, C, D = map(int, input().split())
if A == C: x = -A/2; print(x, x*x+A*x+max(B, D))
else:
    ans = (1e9, 1e9)
    for x in [(D-B)/(A-C), -A/2, -C/2]: ans = min(ans, (x*x+max(A*x+B, C*x+D), x))
    print(*ans[::-1])