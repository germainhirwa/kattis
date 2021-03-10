#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int q,t,b,n,k;
    cin >> q;
    while (q--) {
        cin >> t >> b >> n;
        k = 0;
        while (n) {
            k += (n%b)*(n%b);
            n /= b;
        }
        cout << t << " " << k << endl;
    }

    return 0;
}