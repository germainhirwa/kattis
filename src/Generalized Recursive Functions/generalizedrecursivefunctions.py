import sys

first_input = False
first_line = False
for line in sys.stdin:
    if not first_input:
        first_input = True
    elif not first_line:
        rec = line.split(" ")
        dp = []
        zeroes = [0]*100
        for _ in range(100):
            dp.append(zeroes.copy())
        c = int(rec[-2])
        d = int(rec[-1])
        def f(x,y):
            if x > 0 and y > 0:
                return dp[x][y]
            else:
                return d
        for i in range(100):
            for j in range(100):
                ans = c
                for k in range(len(rec)//2-1):
                    ans += f(i-int(rec[2*k]),j-int(rec[2*k+1]))
                dp[i][j] = ans
        first_line = True
    else: # second line
        queries = line.split(" ")
        for i in range(len(queries)//2):
            print(f(int(queries[2*i]),int(queries[2*i+1])))
        first_line = False
        print()