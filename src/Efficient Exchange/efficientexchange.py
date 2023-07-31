def f(n):x=n%10;m[n]=m[n]if n in m else min(x+f(n//10),10-x+f(n//10+1));return m[n]
m={0:0,1:1};print(f(int(input())))