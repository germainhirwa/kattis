s=m=1
for i in input():s=(5*s+m,2*s+m,2*s,s)[ord(i)%7%4];m*=3*(i<'A')|1
print(s)