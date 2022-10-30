w, s = input(), input()
idx = list(map(int, [s[3*i:3*(i+1)] for i in range(len(s)//3)]))
print(''.join(map(lambda x: w[x-1], idx)))