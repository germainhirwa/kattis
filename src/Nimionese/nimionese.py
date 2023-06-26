ww = input().strip().split()
hards = 'bcdgknptBCDGKNPT'
add = ['ah', 'oh', 'uh']
for i, w in enumerate(ww):
    w = w.split('-')
    hard = min(hards, key=lambda x: (abs(ord(x)-ord(w[0][0])), ord(x.upper())-ord('A')))
    w[0] = hard + w[0][1:]
    if len(w) == 1:
        if w[0][-1] in hards: w[0] += min(add, key=lambda x: (abs(ord(x[0])-ord(w[0][-1])), ord(x[0].upper())-ord('A')))
    else:
        for j, syl in enumerate(w[1:]):
            for k in hards: syl = syl.replace(k, hard.lower() if k.islower() else hard.upper())
            w[j+1] = syl
    ww[i] = ''.join(w)
    if ww[i][-1] in hards: ww[i] += min(add, key=lambda x: (abs(ord(x[0])-ord(ww[i][-1])), ord(x[0].upper())-ord('A')))
print(' '.join(ww))