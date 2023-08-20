a, b, c = map(int, input().split())
vals = [
    a+b-c,
    a-b+c,
    a-b-c,
    a*b+c,
    a*b-c,
    a*b*c,
    (a-b)*c,
    (a+b)*c,
    a//b+c if a%b==0 else 1e9,
    a//b-c if a%b==0 else 1e9,
    (a+b)//c if (a+b)%c==0 else 1e9,
    (a-b)//c if (a-b)%c==0 else 1e9,
    a*b//c if a*b%c==0 else 1e9,
    a//b*c if a%b==0 else 1e9,
    a//b//c if a%b==0 and a//b%c==0 else 1e9
]
print(min(v for v in vals if v >= 0))