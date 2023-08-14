def to_roman(num):
    c = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    x = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    i = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    thousands = 'M'*(num // 1000)
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
    ans = (thousands + hundreds + tens + ones)
    return ans

s = sorted(map(to_roman, range(1, 1001)))
def get_idx(n):
    if n < 1001 and (n > 99 or n < 5 or 49 < n < 90 or n == 9): return s.index(to_roman(n))+1
    elif n < 1001: return s.index(to_roman(n))-1000
    if n%1000:
        base = get_idx(n%1000)
        if base > 0: return 946*(n//1000)+base
        else: return -54*(n//1000)+base
    return 946*(n//1000)

for _ in range(int(input())): print(get_idx(int(input())))