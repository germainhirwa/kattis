a = [int(input()) for _ in range(int(input()))]
print(min(a[i]+a[(i+2)%len(a)] for i in range(len(a))))