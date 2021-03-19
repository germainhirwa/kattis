#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    long d,n; // d = 1, dummy
    char s; // slash
    while (cin >> d >> s >> n) {
        long ans = 1;
        int k = 0, i = 2;
        int m = n;
        while (i <= m) {
            if (n % i == 0) {
                n /= i;
                k++;
            } else { // k is now v_i(n), so i^k is the largest k that divides n
                ans *= 2*k+1;
                k = 0;
                if (i == 2)
                    i++;
                else
                    i += 2;
            }
        }
        cout << (ans+1)/2 << endl;
    }
    return 0;
}