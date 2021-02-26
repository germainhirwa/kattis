#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, q, count;
    cin >> n >> q;

    // Must use bool to avoid MLE (less bits)
    vector<bool> sieve(n+1,true);
    count = n+1;
    int p = 2;
    while (p*p <= n) {
        if (sieve[p]) { // p is guaranteed a prime
            for (int i = 2*p; i < n+1; i += p) { // all multiples of p up to n
                if (sieve[i]) {
                    count--;
                }
                sieve[i] = false;
            }
        }
        p++;
    }

    sieve[1] = false;
    count -= 2; // 0 and 1 are not primes
    cout << count << endl;

    while (q--) {
        int x;
        cin >> x;
        cout << sieve[x] << endl;
    }

    return 0;
}