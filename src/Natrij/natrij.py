h, m, s = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
secs = (3600*(h2-h) + 60*(m2-m) + (s2-s)) % 86400
secs = secs if secs else 86400
dh, dm, ds = secs//3600, (secs%3600)//60, secs%60
print(f'{dh}'.zfill(2)+':'+f'{dm}'.zfill(2)+':'+f'{ds}'.zfill(2))