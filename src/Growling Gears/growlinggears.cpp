#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,n,a,b,c;
    double mt,mi;
    cin >> t;
    while (t--) {
        cin >> n;
        mt = 0;
        mi = 0;
        for (int i = 1; i <= n; i++) {
            cin >> a >> b >> c;
            if (b*b/(4.0*a)+c > mt) {
                mt = b*b/(4.0*a)+c;
                mi = i;
            }
        }
        cout << mi << endl;
    }

    return 0;
}