num = input()
num = num[:6] + num[7:]
check = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
print(int(sum(int(num[i]) * check[i] for i in range(10)) % 11 == 0))