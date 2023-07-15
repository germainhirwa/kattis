class State:
    mem = {}
    def __init__(self, b, t):
        self.b, self.c, self.t = b, [b[::4],b[1::4],b[2::4],b[::5],b[2::3]]+b.split(), t
    def check(self):
        mem = State.mem
        if (self.b, self.t) in mem: return mem[(self.b, self.t)]
        x_win = 'xxx' in self.c
        o_win = 'ooo' in self.c
        assert not (x_win and o_win)
        mem[(self.b, self.t)] = 1 if x_win else -1 if o_win else 0
        return mem[(self.b, self.t)]
    def end(self):
        return str(self.check() or '.' not in self.b)
    def nxt(self):
        s = []
        r = [list(i) for i in self.b.split()]
        for i in range(3):
            for j in range(3):
                if r[i][j] == '.':
                    r[i][j] = 'ox'[self.t]
                    s.append(State('\n'.join(''.join(w) for w in r), 1-self.t))
                    r[i][j] = '.'
        return s

ttt = open(0).read().replace(' ', '').replace('_', '.').lower().strip()
initial_turn = 1 - ttt.count('x') + ttt.count('o')
initial_state = State(ttt, initial_turn)
x_can_win, o_can_win = False, False
stack = [initial_state]
while stack:
    state = stack.pop()
    end = state.end()
    if end == '1': x_can_win = True; continue
    elif end == '-1': o_can_win = True; continue
    elif end == 'True': continue
    for i in state.nxt(): stack.append(i)
if x_can_win and o_can_win: print('Abdullah och Johan kan vinna')
elif x_can_win: print('Johan kan vinna')
elif o_can_win: print('Abdullah kan vinna')
else: print('ingen kan vinna')