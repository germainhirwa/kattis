n = int(input())

def similar(a,b):
    k = min(len(a),len(b))
    for i in range(k):
        if a[i] != b[i]:
            return i
    return k

for _ in range(n):
    w = input()
    written = input()
    s1 = input()
    s2 = input()
    s3 = input()
    
    a1 = len(w) + len(written) - 2*similar(w,written)
    a2 = len(w) + len(s1) - 2*similar(w,s1) + 1
    a3 = len(w) + len(s2) - 2*similar(w,s2) + 1
    a4 = len(w) + len(s3) - 2*similar(w,s3) + 1

    print(min(a1,a2,a3,a4))