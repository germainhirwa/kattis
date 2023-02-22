a, d, r, t = 4, *[int(input()) for _ in range(3)]
while a*(a+1)+(a-d)*(a-d+1) != 2*(r+t+9): a += 1
print(r+6-a*(a+1)//2)