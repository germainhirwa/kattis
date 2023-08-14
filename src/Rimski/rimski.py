def to_roman(num):
    m = ['', 'M', 'MM', 'MMM', 'MMMM']
    c = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    x = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    i = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
    ans = (thousands + hundreds + tens + ones)
    return ans
r = [*map(to_roman, range(1, 101))]
from itertools import permutations
s = input(); print(min({*map(''.join, permutations(s))}&{*r}, key=r.index))