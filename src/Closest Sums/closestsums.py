def closest_sum(m, nums):
    m_sum = float("inf")
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if abs(nums[i]+nums[j]-m) <= abs(m_sum-m):
                m_sum = nums[i]+nums[j]
    return f'Closest sum to {m} is {m_sum}.'

case = 1

try:
    while True:
        n = int(input())
        nums = []
        for _ in range(n):
            nums.append(int(input()))

        m = int(input())
        nums.sort()
        print(f'Case {case}:')
        for _ in range(m):
            print(closest_sum(int(input()),nums))
        case += 1
except:
    pass