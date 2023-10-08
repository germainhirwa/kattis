h = {'Shadow': 6, 'Gale': 5, 'Ranger': 4, 'Anvil': 7, 'Vexia': 3, 'Guardian': 8, 'Thunderheart': 6, 'Frostwhisper': 2, 'Voidclaw': 3, 'Ironwood': 3, 'Zenith': 4, 'Seraphina': 1}
b = [input().split()[1:] for _ in range(6)]; oo = [0, 0]; tt = [0, 0]
for p, (o, t) in enumerate(zip(b[::2], b[1::2])):
    oc = tc = 0
    for c in o:
        oc += h[c]
        if c == 'Thunderheart' and len(o) == 4: oc += h[c]
        elif p == 1 and c == 'Zenith': oc += 5
        elif c == 'Seraphina': oc += len(o)-1
    for c in t:
        tc += h[c]
        if c == 'Thunderheart' and len(t) == 4: tc += h[c]
        elif p == 1 and c == 'Zenith': tc += 5
        elif c == 'Seraphina': tc += len(t)-1
    oo[1] += oc; tt[1] += tc
    if oc > tc: oo[0] += 1
    elif oc < tc: tt[0] += 1
if oo > tt: print('Player 1')
elif oo < tt: print('Player 2')
else: print('Tie')