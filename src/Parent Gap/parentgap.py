def ly(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
curr, may, yr = 2000, 14, int(input())
while curr != yr:
    curr += 1
    may -= 1+ly(curr)
    may = may%7+7 if may%7 else 14
print(((may+4)%7+45-may if (may+4)%7 else 52-may)//7, 'weeks')