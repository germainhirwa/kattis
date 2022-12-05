angles = {}
for h in range(12):
    for m in range(60):
        hp = 30*h + m/2
        mp = 6*m
        angles[(hp - mp) % 360] = f'{str(h).zfill(2)}:{str(m).zfill(2)}'
print(angles[-int(input())/10 % 360])