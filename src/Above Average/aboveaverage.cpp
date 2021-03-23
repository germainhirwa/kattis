#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,l,s,a,p;
    cin >> t;
    while (t--) {
        a = 0;
        p = 0;
        cin >> l;
        int sc[l];
        for (int i = 0; i < l; i++) {
            cin >> s;
            sc[i] = s;
            a += s;
        }
        for (int i = 0; i < l; i++) {
            if (l*sc[i] > a)
                p++;
        }
        cout << fixed << setprecision(3) << 100.0*p/l << "%" << endl;
    }

    return 0;
}