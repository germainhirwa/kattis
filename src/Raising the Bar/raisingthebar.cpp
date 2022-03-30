#include <bits/stdc++.h>
using namespace std;

const int LIMIT = 1000001;

long long pow(long long x, long long y, long long p) {
    long long res = 1;
    x = x % p;
    if (x == 0)
        return 0;

    while (y > 0) {
        if (y & 1)
            res = (res * x) % p;
        y = y >> 1;
        x = (x*x) % p;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    vector<bool> sieve(LIMIT+1,true);
    vector<int> primes;
    int p = 2;
    while (p <= LIMIT) {
        if (sieve[p]) { // p is guaranteed a prime
            primes.push_back(p);
            for (int i = 2*p; i < LIMIT+1; i += p) { // all multiples of p up to n
                sieve[i] = false;
            }
        }
        p++;
    }

    long long n, d, dd;
    cin >> n >> d;

    dd = d;
    while (dd % 2 == 0)
        dd /= 2;
    while (dd % 5 == 0)
        dd /= 5;

    if (dd != 1) {
        long long tot = dd;
        for (int i : primes) {
            if (tot % i == 0) {
                tot *= (i - 1);
                tot /= i;
            }
        }
        
        vector<long long> div;
        long long xx = 1;
        while (xx * xx <= tot) {
            if (tot % xx == 0) {
                div.push_back(xx);
                if (xx * xx != tot)
                    div.push_back(tot / xx);
            }
            xx++;
        }
        sort(div.begin(), div.end());

        int ord = 1;
        for (int dv : div) {
            if (pow(10, dv, dd) == 1) {
                ord = dv;
                break;
            }
        }

        long long v = (n * (pow(10, ord, d) - 1)) % d;
        int m = 0;
        while (v % d != 0) {
            m++;
            v = (10 * v) % d;
        }
        cout << m << ' ' << ord;
    } else {
        int m = 0;
        while (n % d != 0) {
            m++;
            n = (10 * n) % d;
        }
        cout << m << ' ' << 0;
    }

    return 0;
}