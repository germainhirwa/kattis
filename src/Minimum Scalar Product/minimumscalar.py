n = int(input())
for i in range(n):
    k = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    msp = 0
    a.sort()
    b.sort(reverse = True)
    for j in range(k):
        msp += a[j]*b[j]
    print(f"Case #{i+1}: {msp}")