import sys

# DP Version
"""
dp_table = {(0,0,0):1}
def dp(x,y,s):
    if s == 0:
        dp_table[(x,y,0)] = dp_table.get((x,y,0),0)
        return dp_table[(x,y,0)]
    else:
        if (x,y,s) not in dp_table:
            dp_table[(x,y,s)] = dp(x,y-1,s-1) + dp(x,y+1,s-1) + dp(x-1,y,s-1) + dp(x+1,y,s-1) + dp(x-1,y-1,s-1) + dp(x+1,y+1,s-1)
        return dp_table[(x,y,s)]
"""

i = 0
answer = [0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 1588356, 8676360, 47977776, 266378112, 1488801600]
for line in sys.stdin:
    if i == 0:
        i = line
    else:
        # print(dp(0,0,int(line)))
        print(answer[int(line)-1])