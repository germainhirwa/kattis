import string

abc = '''clank
bong
click
tap
poing
clonk
clack
ping
tip
cloing
tic
cling
bing
pong
clang
pang
clong
tac
boing
boink
cloink
rattle
clock
toc
clink
tuc'''.split()

caps = [0]

def cl(): caps[0] = 1-caps[0]
def p(): log.pop() if log else 0

d = {i:j for i, j in zip(abc, string.ascii_lowercase)}
d['whack'] = ' '
d['bump'] = d['dink'] = d['thumb'] = cl
d['pop'] = p

log = []
for _ in range(int(input())):
    s = d[input().strip()]
    if type(s) == type(cl): s()
    else: log.append(s.upper() if caps[0] else s)
print(''.join(log))