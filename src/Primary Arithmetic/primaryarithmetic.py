import sys

def check(a, b, carry=0):
    if a == b == 0: return 0
    last = (a % 10 + b % 10 + carry)
    return check(a // 10, b // 10, last // 10) + (last > 9)

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == b == 0: break
    carry = check(a, b)
    if carry > 1:   print(f"{carry} carry operations.")
    elif carry:     print(f"{carry} carry operation.")
    else:           print("No carry operation.")