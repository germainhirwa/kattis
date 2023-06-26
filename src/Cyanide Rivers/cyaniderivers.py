from math import ceil
s = input().strip()
idx = [i for i in range(len(s)) if s[i] == '1']
try: print(ceil(max(b-a-1 for a,b in zip(idx, idx[1:]))/2))
except: print(0)