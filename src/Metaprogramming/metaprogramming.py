reg = {}
for line in open(0).readlines():
    cmd = line.strip().split()
    if cmd[0] == 'define':
        reg[cmd[2]] = int(cmd[1])
    else:
        exp = f'reg["{cmd[1]}"] {cmd[2]} reg["{cmd[3]}"]'.replace('=', '==')
        try:    print(str(eval(exp)).lower())
        except: print('undefined')