from datetime import *
dat = {}; dt = datetime(2023, 1, 1)
for i in range(365): dat[(dt+timedelta(days=i)).strftime('%m-%d')] = i
b = sorted({*(dat[input().split()[1]] for _ in range(int(input())))})
b.append(b[0]+365); best = (-1, -1, -1)
for i in range(1, len(b)): best = max(best, (b[i]-b[i-1], -(b[i]-300)%365, i))
print((dt+timedelta(days=b[best[2]]%365-1)).strftime('%m-%d'))