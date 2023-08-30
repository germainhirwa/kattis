for tc in range(1, int(input())+1):
    T = int(input())
    NA, NB = map(int, input().split())
    da, db, aa, ab = [], [], [], []
    for _ in range(NA):
        a, b = input().split()
        ha, ma = map(int, a.split(':'))
        hb, mb = map(int, b.split(':'))
        da.append(60*ha+ma), ab.append(60*hb+mb+T)
    for _ in range(NB):
        a, b = input().split()
        ha, ma = map(int, a.split(':'))
        hb, mb = map(int, b.split(':'))
        db.append(60*ha+ma), aa.append(60*hb+mb+T)
    da.sort(reverse=True), db.sort(reverse=True), aa.sort(reverse=True), ab.sort(reverse=True)
    A = B = 0
    while da:
        if aa and da[-1] >= aa[-1]: aa.pop()
        else: A += 1
        da.pop()
    while db:
        if ab and db[-1] >= ab[-1]: ab.pop()
        else: B += 1
        db.pop()
    print(f'Case #{tc}:', A, B)