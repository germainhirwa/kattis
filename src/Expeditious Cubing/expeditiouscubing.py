prec = 10**10
t = [*map(lambda x: round(prec*float(x)), input().split())]; x = round(prec*float(input()))
mi, ma, s = min(t), max(t), sum(t)
if 3*x+mi >= s: print('infinite')
elif 3*x+ma < s: print('impossible')
else: print("%.2f"%((3*x-s+mi+ma)/prec))