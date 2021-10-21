n = int(input())

c = 1
import sys

def num_to_base(num, base_str):
    res = []
    while num:
        res.append(base_str[num % len(base_str)])
        num //= len(base_str)
    return str().join(res)[::-1]
    
def base_to_num(b, base_str): # b = "0111", base_str = "01", returns 7
    res = 0
    for d in b:
        res *= len(base_str)
        res += base_str.find(d)
    return res

for line in sys.stdin:
    n, src, dest = line.strip().split()
    bs, bd = len(src), len(dest)
    print(f"Case #{c}: {num_to_base(base_to_num(n, src), dest)}")
    c += 1