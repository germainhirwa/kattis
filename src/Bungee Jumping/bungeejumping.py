import sys
for i in sys.stdin:
    k, l, s, w = map(float, i.split())
    if k+l+s+w == 0: break
    t_hit = (2*s/9.81)**0.5
    t_rope = (2*l/9.81)**0.5
    if t_hit <= t_rope: print(['James Bond survives.', 'Killed by the impact.'][9.81*t_hit > 10])
    else:
        dt = 1e-5
        t = t_rope; d = 4.905*t**2; v = 9.81*t
        for _ in range(200_000):
            a = 9.81-k*max(d-l, 0)/w
            t += dt; v2 = v; v += a*dt; d += 0.5*(v+v2)*dt
            if d >= s: break
        if d >= s: print(['James Bond survives.', 'Killed by the impact.'][v > 10])
        else: print('Stuck in the air.')