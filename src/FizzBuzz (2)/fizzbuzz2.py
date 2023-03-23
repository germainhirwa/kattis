def fizzbuzz(i):
    if i % 15 == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        return str(i)

def gen_fizzbuzz(n):
    return [fizzbuzz(i) for i in range(1, n + 1)]

def match(arr1, arr2):
    return sum(int(arr1[i] == arr2[i]) for i in range(len(arr1)))

import sys
curr, ctr, ans = 0, 1, 1
skip = input()
for line in sys.stdin:
    check = line.strip().split()
    k = match(check, gen_fizzbuzz(len(check)))
    if k > curr:
        ans, curr = ctr, k
    ctr += 1
print(ans)