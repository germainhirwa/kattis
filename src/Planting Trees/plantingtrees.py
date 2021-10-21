n = int(input())
days = list(map(int, input().split()))
days.sort(reverse=True)

m_days = 0
for i in range(n):
    m_days = max(m_days, days[i] + i + 2)
print(m_days)