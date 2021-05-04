#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,n,m,u,v;
    cin >> t;
    while (t--) {
        cin >> n >> m;
        while (m--)
            cin >> u >> v;
        cout << n-1 << endl;
    }

    return 0;
}