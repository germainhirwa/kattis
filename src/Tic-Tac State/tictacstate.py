n = int(input())
for _ in range(n):
    state = bin(int(input(), 8))[:1:-1]
    state += '0'*(18 - len(state))
    def check():
        for i in range(3):
            if state[3*i] == state[3*i+1] == state[3*i+2] == '1':
                i += 3
                cs = state[3*i] + state[3*i+1] + state[3*i+2]
                if cs == '111':
                    return 'X wins'
                elif cs == '000':
                    return 'O wins'
        for i in range(3):
            if state[i] == state[i+3] == state[i+6] == '1':
                i += 9
                cs = state[i] + state[i+3] + state[i+6]
                if cs == '111':
                    return 'X wins'
                elif cs == '000':
                    return 'O wins'
        for x, y, z in [[0,4,8], [2,4,6]]:
            if state[x] == state[y] == state[z] == '1':
                cs = state[x + 9] + state[y + 9] + state[z + 9]
                if cs == '111':
                    return 'X wins'
                elif cs == '000':
                    return 'O wins'
        return ["Cat's", 'In progress'][int(state.find('0') in range(9))]
    print(check())