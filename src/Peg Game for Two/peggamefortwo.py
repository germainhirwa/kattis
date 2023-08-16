valid = [[(1, 3), (2, 5)], [(3, 6), (4, 8)], [(4, 7), (5, 9)], [(1, 0), (4, 5), (6, 10), (7, 12)], [(7, 11), (8, 13)], [(2, 0), (4, 3), (8, 12), (9, 14)], [(3, 1), (7, 8)], [(4, 2), (8, 9)], [(4, 1), (7, 6)], [(5, 2), (8, 7)], [(6, 3), (11, 12)], [(7, 4), (12, 13)], [(7, 3), (8, 5), (11, 10), (13, 14)], [(8, 4), (12, 11)], [(9, 5), (13, 12)]]

class State:
    def __init__(self, peg, turn, score):
        self.peg = peg; self.turn = turn; self.score = score
        self.next = None
    def check(self):
        return self.score[0]-self.score[1]
    def end(self):
        if self.next == None: self.next = self.nxt()
        return not self.next
    def nxt(self):
        if self.next != None: return self.next
        s = []
        for i in range(15):
            if self.peg[i]: continue
            for j, k in valid[i]:
                if self.peg[j] and self.peg[k]:
                    old = self.peg[j]
                    self.peg[j] = 0
                    self.peg[i], self.peg[k] = self.peg[k], self.peg[i]
                    self.score[self.turn] += self.peg[i]*old
                    s.append(State(self.peg.copy(), 1-self.turn, self.score.copy()))
                    self.score[self.turn] -= self.peg[i]*old
                    self.peg[i], self.peg[k] = self.peg[k], self.peg[i]
                    self.peg[j] = old
        self.next = s; return s

def max_value(state, alpha, beta, depth):
    if state.end() or depth == 0: return state.check(), None
    v = -float('inf')
    for a in state.nxt():
        v2, _ = min_value(a, alpha, beta, depth-1)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta: return v, move
    return v, move

def min_value(state, alpha, beta, depth):
    if state.end() or depth == 0: return state.check(), None
    v = float('inf')
    for a in state.nxt():
        v2, _ = max_value(a, alpha, beta, depth-1)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha: return v, move
    return v, move

peg = []
for _ in range(5): peg.extend(map(int, input().split()))
print(max_value(State(peg, 0, [0, 0]), -float('inf'), float('inf'), 11)[0])