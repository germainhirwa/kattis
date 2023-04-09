from random import randint, seed
from math import hypot
from time import time

def cost(G, s):
    l = 0
    for i in range(N-1): l += G[s[i]][s[i+1]]
    l += G[s[-1]][s[0]]
    return l

def tsp_greedy(G):
    used = [0]*N
    tour = [0]
    used[0] = 1
    for i in range(1, N):
        best =  -1
        for j in range(N):
            if not used[j] and (best == -1 or G[tour[i-1]][j] < G[tour[i-1]][best]): best = j
        tour.append(best)
        used[best] = True
    return tour

def tsp_k_opt(G, asp_ratio=2, tabu_tenure=7):
    tour = tsp_greedy(G)
    best_tour, best_cost = tour, cost(G, tour)

    def _4_opt(tour):
        a = randint(1, N//4)
        b = a + randint(1, N//4)
        c = b + randint(1, N//4)
        return [*tour[:a], *tour[c:], *tour[b:c], *tour[a:b]]

    def _2_opt(tour, asp_ratio, tabu_tenure, TIME_LIMIT):
        def decrement_tabu():
            k = N//2
            for i in range(k):
                for j in range(k):
                    if tabu_list[i][j] > 0: tabu_list[i][j] = tabu_list[j][i] = tabu_list[i][j] - 1

        tabu_list = [[0]*N for _ in range(N)]
        original_tour = local_opt_tour = list(tour)
        original_cost = local_opt_cost = cost(G, tour)
        best_cost, tour = original_cost, original_tour
        while time() - t <= TIME_LIMIT:
            is_local_opt = False
            while not is_local_opt and time() - t <= TIME_LIMIT:
                is_local_opt = True
                for i in range(N):
                    for k in range(i+1, N-1):
                        iB = N-1 if i == 0 else i-1
                        kA = 0 if k == N-1 else k+1
                        new_cost = best_cost - G[tour[i]][tour[iB]] - G[tour[k]][tour[kA]] + G[tour[iB]][tour[k]] + G[tour[i]][tour[kA]]
                        if (new_cost < best_cost and tabu_list[i][k] == 0) or new_cost * asp_ratio < best_cost:
                            if i == 0:  tour = [*tour[:i], *tour[k::-1], *tour[k+1:]]
                            else:       tour = [*tour[:i], *tour[k:i-1:-1], *tour[k+1:]]
                            best_cost = new_cost
                            is_local_opt = False
                            tabu_list[i][k] = tabu_tenure
                        if time() - t > TIME_LIMIT: return tour
                    if time() - t > TIME_LIMIT: return tour
                decrement_tabu()
            if best_cost < local_opt_cost:
                local_opt_tour = tour
                local_opt_cost = best_cost
        return local_opt_tour

    def _2half_opt(tour, TIME_LIMIT):
        can_improve = True
        while can_improve and time() - t <= TIME_LIMIT:
            can_improve = False
            for i in range(N-2):
                for j in range(i+3, N-1):
                    a, b, c, d, e = *tour[i:i+3], *tour[j:j+2]
                    if G[a][c] + G[d][b] + G[b][e] < G[a][b] + G[b][c] + G[d][e]:
                        can_improve = True
                        tour = [*tour[:i+1], *tour[i+2:j+1], tour[i+1], *tour[j+1:]]
                    if time() - t > TIME_LIMIT: return tour
                if time() - t > TIME_LIMIT: return tour
        return tour

    def _3_opt(tour, TIME_LIMIT):
        can_improve = True
        best_cost = cost(G, tour)
        while can_improve and time() - t <= TIME_LIMIT:
            can_improve = False
            for i in range(1, N):
                for j in range(i+1, N):
                    rem = best_cost - (G[tour[i]][tour[i-1]] + G[tour[j]][tour[j-1]] + G[tour[N-1]][tour[0]])
                    t1_cost = rem + G[tour[i-1]][tour[j]] + G[tour[N-1]][tour[i]] + G[tour[j-1]][tour[0]]
                    t2_cost = rem + G[tour[i-1]][tour[j-1]] + G[tour[N-1]][tour[i]] + G[tour[j]][tour[0]]
                    best_cost = min(t1_cost, t2_cost, best_cost)
                    if t1_cost == best_cost:
                        can_improve = True
                        best_cost = t1_cost
                        tour = [*tour[:i], *tour[j:], *tour[i:j]]
                    elif t2_cost == best_cost:
                        can_improve = True
                        best_cost = t2_cost
                        tour = [*tour[:i], *tour[j-1:i-1:-1], *tour[:j-1:-1]]
                    if time() - t > TIME_LIMIT: return tour
                if time() - t > TIME_LIMIT: return tour
        return tour

    t = time()
    while time() - t < 1.8:
        #tour = _4_opt(tour)
        tour = _2_opt(tour, asp_ratio, tabu_tenure, 1.8)
        tour = _2half_opt(tour, 1.8)
        tour = _3_opt(tour, 1.8)
        c = cost(G, tour)
        if c < best_cost: best_tour, best_cost = tour, c
    return best_tour

N = int(input())
if N < 4:
    for i in range(N): print(i)
else:
    p = [list(map(float, input().split())) for _ in range(N)]
    G = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N): G[i][j] = G[j][i] = round(hypot(p[i][0]-p[j][0], p[i][1]-p[j][1]))
    s = tsp_k_opt(G)
    [*map(print, s)]; #print('Greedy cost:', cost(G, tsp_greedy(G))); print('k-opt:'.ljust(12), cost(G, s))