import sys

p = {}
fl = True
for line in sys.stdin:
    if fl:
        r = int(line)
        fl = False
    else:
        nums = list(map(int,line.split(" ")))
        if len(nums) != 1:
            for v in nums[1:]:
                p[v] = nums[0]
        
while r in p:
    print(r,end=" ")
    r = p[r]
print(r)