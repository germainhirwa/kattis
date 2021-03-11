#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t, m, c, s = 0, p = 2;
    vector<int> v;
    cin >> t;
    while (t--) {
        cin >> m;
        v.push_back(m);
        s = max(s,m);
    }

    // Must use bool to avoid MLE (less bits)
    vector<bool> sieve(s,true);
    while (p*p <= s) {
        if (sieve[p]) { // p is guaranteed a prime
            for (int i = 2*p; i < s; i += p) { // all multiples of p up to n
                sieve[i] = false;
            }
        }
        p++;
    }

    for (int n : v) {
        c = 0;
        for (int i = 2; i <= n/2; i++) {
            if (sieve[i] && sieve[n-i]) {
                c++;
            }
        }
        cout << n << " has " << c << " representation(s)" << endl;
        for (int i = 2; i <= n/2; i++) {
            if (sieve[i] && sieve[n-i]) {
                cout << i << "+" << n-i << endl;
            }
        }
        cout << endl;
    }

    return 0;
}