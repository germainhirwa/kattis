#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, q, count;
    cin >> n >> q;

    // Must use bool to avoid MLE (less bits)
    vector<bool> sieve(n+1,true);
    count = 0;
    int p = 2;
    while (p*p <= n) {
        if (sieve[p]) { // p is guaranteed a prime
            for (int i = p; i < n+1; i += p) { // all multiples of p up to n
                if (sieve[i]) {
                    count++;
                }
                sieve[i] = false;
                if (count == q) {
                    cout << i;
                    return 0;
                }
            }
        }
        p++;
    }
    while (count != q) {
        if (sieve[p]) {
            count++;
        }
        if (count == q) {
            cout << p;
            return 0;
        }
        p++;
    }

    return 0;
}