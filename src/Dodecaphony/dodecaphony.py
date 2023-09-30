h = {e:i for i,e in enumerate(['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'])}
input(); a = [h[i] for i in input().split()]; b = [h[i] for i in input().split()]
if a == b[::-1]: print('Retrograde')
elif len({(x-y)%12 for x,y in zip(a,b)}) == 1: print('Transposition')
else:
    f = a[0]; inv = a[0]==b[0]
    for i in range(1, len(a)):
        if (a[i]-f)%12 != (f-b[i])%12: inv = 0
    print(['Nonsense', 'Inversion'][inv])