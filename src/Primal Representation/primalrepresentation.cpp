#include <bits/stdc++.h>

#define INF INT_MAX
#define pb push_back
#define ub upper_bound
#define lb lower_bound

using namespace std;
using ll = long long;
using vi = vector<int>;
using vl = vector<long>;
using vll = vector<long long>;
using vvi = vector<vector<int>>;
using vvl = vector<vector<long>>;
using vvll = vector<vector<long long>>;
using mii = map<int, int>;
using pii = pair<int, int>;
using plli = pair<long long, int>;

const int LIMIT = 1 << 15 + 1;

plli vee(ll n, int p) {
    int v = 0;
    while (n % p == 0) {
        n /= p;
        v++;
    }
    return plli(n, v);
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    
    ll k;
    vll v;
    vi primes;
    while (cin >> k)
        v.pb(k);

    bool sieve[LIMIT];
    for (int i = 0; i < LIMIT; i++)
        sieve[i] = true;
    int p = 2;
    while (p < LIMIT) {
        if (sieve[p]) {
            primes.pb(p);
            for (int i = 2*p; i < LIMIT; i += p)
                sieve[i] = false;
        }
        if (p == 2)
            p--;
        p += 2;
    }

    for (ll n : v) {
        if (n < 0) {
            n = -n;
            cout << -1 << ' ';
        }

        for (int p : primes) {
            if (n % p == 0) {
                plli nk = vee(n, p);
                n = nk.first;
                k = nk.second;
                if (k == 1)
                    cout << p << ' ';
                else
                    cout << p << '^' << k << ' ';
            }
        }

        if (n != 1)
            cout << n;
        cout << '\n';
    }

    return 0;
}