y = int(input())
m = 4
have = False
for i in range(1, 13):
    if ((y - 2018)*12 + i) % 26 == 4:
        have = True
        break
print(["no", "yes"][int(have)])