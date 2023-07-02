N = int(input())
lp, phi, pr = [0]*(N+1), [0]*(N+1), []
phi[1] = 1
for i in range(2, N+1):
    if not lp[i]: lp[i], phi[i] = i, i-1; pr.append(i)
    else: phi[i] = phi[i // lp[i]] * (lp[i] - (lp[i] != lp[i // lp[i]]))
    j = 0
    while j < len(pr) and pr[j] <= lp[i] and i*pr[j] <= N: lp[i*pr[j]] = pr[j]; j += 1
print(sum(phi[q]*(N//q)*(N//q+1) for q in range(2, N+1))//2)