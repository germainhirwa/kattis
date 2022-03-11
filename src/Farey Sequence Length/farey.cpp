#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    // prime sieve
    int limit = 1e8;
    vector<bool> sieve(limit + 1, true);
    vector<int> primes;
    int p = 2;
    while (p*p <= limit + 1) {
        if (sieve[p]) { // p is guaranteed a prime
            primes.push_back(p);
            for (int i = 2*p; i < limit + 1; i += p) { // all multiples of p up to limit
                sieve[i] = false;
            }
        }
        p++;
    }

    sieve[1] = false;
    int q, x;
    int rs[10001] {0};

    for (int i = 1; i < 10001; i++) {
        int t = i, n = i;
        if (sieve[i]) {
            rs[i] = rs[i - 1] + (i - 1);
        } else {
            for (int pp : primes) {
                if (t % pp == 0) {
                    t /= pp;
                    n *= (pp - 1);
                    n /= pp;
                }
            }
            rs[i] = rs[i - 1] + n;
        }
    }

    cin >> q;
    while (q--) {
        int c, x;
        cin >> c >> x;
        cout << c << " " << rs[x] + 1 << endl;
    }

    return 0;
}