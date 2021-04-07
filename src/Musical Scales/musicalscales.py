import sys

# A , A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯

# tone to number
music = {
    'A':0,
    'A#':1,
    'B':2,
    'C':3,
    'C#':4,
    'D':5,
    'D#':6,
    'E':7,
    'F':8,
    'F#':9,
    'G':10,
    'G#':11
}

# number to tone
music2 = dict(map(lambda x:(x[1],x[0]), music.items()))

for line in sys.stdin:
    try:
        x = int(line)
    except:
        tones = list(line.strip().split(" "))
        possible = [x]*12
        for t in tones:
            for k in [0,2,4,5,7,9,11]:
                possible[(music[t]-k)%12] -= 1

        if 0 not in possible:
            print('none')
        else:
            for i in range(12):
                if possible[i] == 0:
                    print(music2[i],end=' ')