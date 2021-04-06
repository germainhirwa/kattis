#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    long t, ncs, ne, e, ans, scs, se;
    
    cin >> t;
    while (t--) {
        cin >> ncs >> ne;
        int cs[ncs];

        scs = 0;
        se = 0;

        for (int i = 0; i < ncs; i++) {
            cin >> cs[i];
            scs += cs[i];
        }

        for (int i = 0; i < ne; i++) {
            cin >> e;
            se += e;
        }

        ans = 0;
        for (int i = 0; i < ncs; i++)
            if (scs > cs[i]*ncs && cs[i]*ne > se)
                ans++;

        cout << ans << endl;
    }

    return 0;
}