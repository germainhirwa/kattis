# https://codegolf.stackexchange.com/questions/79691/calculate-the-fermat-point-of-a-triangle
from math import *;p=2*pi/3
A,B,C=[[*map(int, input().split())]for _ in range(3)]
d=lambda x,y:hypot(x[0]-y[0],x[1]-y[1])
s=lambda A,B,C:(d(B,C),d(C,A),d(A,B))
j=lambda a,b,c:acos((b*b+c*c-a*a)/(2*b*c))
t=lambda a,b,c:1/cos(j(a,b,c)-pi/6)
b=lambda A,B,C,p,q,r:[(p*A[i]+q*B[i]+r*C[i])/(p+q+r)for i in[0,1]] 
print(*(A if j(*s(A,B,C))>=p else B if j(*s(B,C,A))>=p else C if j(*s(C,A,B))>=p else b(A,B,C,d(B,C)*t(*s(A,B,C)),d(C,A)*t(*s(B,C,A)),d(A,B)*t(*s(C,A,B)))))