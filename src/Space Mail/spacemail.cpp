#include <bits/stdc++.h>
#define pb push_back
using namespace std;
using ll = long long;
using vi = vector<int>;
using vl = vector<long>;
using vll = vector<long long>;
using mii = map<int, int>;
using mivll = map<int, vector<long long>>;

class UnionFind {
    private:
        vi parent;
        vi rank;
        int numSets;

    public:
        UnionFind(int N) {
            for (int i = 0; i < N; i++) {
                parent.pb(i);
                rank.pb(0);
            }
            numSets = N;
        }

        int findSet(int i) {
            if (parent[i] == i)
                return i;
            return parent[i] = findSet(parent[i]);
        }

        bool isSameSet(int i, int j) {
            return findSet(i) == findSet(j);
        }

        void unionSet(int i, int j) {
            if (!isSameSet(i, j)) {
                numSets--;
                int x = findSet(i), y = findSet(j);
                if (rank[x] > rank[y]) {
                    parent[y] = x;
                    if (rank[x] == rank[y])
                        rank[x]++;
                } else {
                    parent[x] = y;
                    if (rank[x] == rank[y])
                        rank[y]++;
                }
            }
        }

        int numDisjointSets() {
            return numSets;
        }
};

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n, x, y, z, mm = 0, dist = 0;
    cin >> n;
    UnionFind ufds(n);
    mii rev;
    mivll dists;

    while (n--) {
        cin >> x >> y >> z;
        ll p1 = 1002001 * x + 1001 * y + z;
        for (const auto& p : rev) {
            long p2 = p.first;
            int dist = (int) ceil(sqrt(
                (z - p2 % 1001) * (z - p2 % 1001) +
                (y - p2 / 1001 % 1001) * (y - p2 / 1001 % 1001) +
                (x - p2 / 1002001 % 1001) * (x - p2 / 1002001 % 1001)
            ));
            if (dists.find(dist) == dists.end()) {
                vll nv;
                dists[dist] = nv;
            }
            dists[dist].pb(1003003001 * p1 + p2);
        }
        rev[p1] = n;
    }

    while (true) {
        if (dists.find(dist) != dists.end()) {
            for (ll h : dists[dist]) {
                int p1 = (int) (h / 1003003001), p2 = (int) (h % 1003003001);
                if (!ufds.isSameSet(rev[p1], rev[p2])) {
                    mm = max(mm, dist);
                    ufds.unionSet(rev[p1], rev[p2]);
                }
                if (ufds.numDisjointSets() == 1) {
                    cout << mm;
                    return 0;
                }
            }
        }
        dist++;
    }
}