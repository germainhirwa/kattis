#include <iostream>
#include <math.h>

using namespace std;

int main() {
    long a,b,t,n,k,MOD = 1000000007;
    cin >> t;
    while (t--) {
        a = 1, b = 1;
        cin >> n;
        while (n--) {
            k = (a+b) % MOD;
            a = b;
            b = k;
        }
        cout << b << endl;
    }
    return 0;
}