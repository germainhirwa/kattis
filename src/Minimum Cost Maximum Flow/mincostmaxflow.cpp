// https://github.com/stevenhalim/cpbook-code/blob/master/ch9/mcmf.cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef tuple<int, ll, ll, ll> edge;
typedef vector<int> vi;
typedef vector<ll> vll;

const ll INF = 1e18;

class min_cost_max_flow {
private:
    int V;
    ll total_cost;
    vector<edge> EL;
    vector<vi> AL;
    vll d;
    vi last, vis;

    bool SPFA(int s, int t) {
        d.assign(V, INF); d[s] = 0; vis[s] = 1;
        queue<int> q({s});
        while (!q.empty()) {
            int u = q.front(); q.pop(); vis[u] = 0;
            for (auto &idx : AL[u]) {
                auto &[v, cap, flow, cost] = EL[idx];
                if ((cap-flow > 0) && (d[v] > d[u] + cost)) {
                    d[v] = d[u]+cost;
                    if(!vis[v]) q.push(v), vis[v] = 1;
                }
            }
        }
        return d[t] != INF;
    }

    ll DFS(int u, int t, ll f = INF) {
        if ((u == t) || (f == 0)) return f;
        vis[u] = 1;
        for (int &i = last[u]; i < (int)AL[u].size(); ++i) {
            auto &[v, cap, flow, cost] = EL[AL[u][i]];
            if (!vis[v] && d[v] == d[u]+cost) {
                if (ll pushed = DFS(v, t, min(f, cap-flow))) {
            total_cost += pushed * cost;
                    flow += pushed;
                    auto &[rv, rcap, rflow, rcost] = EL[AL[u][i]^1];
                    rflow -= pushed;
                    vis[u] = 0;
                    return pushed;
                }
            }
        }
        vis[u] = 0;
        return 0;
    }

public:
    min_cost_max_flow(int initialV) : V(initialV), total_cost(0) {
        EL.clear();
        AL.assign(V, vi());
        vis.assign(V, 0);
    }

    void add_edge(int u, int v, ll w, ll c, bool directed = true) {
        if (u == v) return;
        EL.emplace_back(v, w, 0, c);
        AL[u].push_back(EL.size()-1);
        EL.emplace_back(u, 0, 0, -c);
        AL[v].push_back(EL.size()-1);
        if (!directed) add_edge(v, u, w, c);
    }

    pair<ll, ll> mcmf(int s, int t) {
        ll mf = 0;
        while (SPFA(s, t)) {
            last.assign(V, 0);
            while (ll f = DFS(s, t))
                mf += f;
        }
        return {mf, total_cost};
    }
};

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    int V, E, s, t, u, v, w, c;
    cin >> V >> E >> s >> t;
    min_cost_max_flow mf(V);
    for (int i = 0; i < E; ++i) {
        cin >> u >> v >> w >> c;
        mf.add_edge(u, v, w, c);
    }
    pair<ll, ll> res = mf.mcmf(s, t);
    printf("%lld %lld\n", res.first, res.second);
    return 0;
}