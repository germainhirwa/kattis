#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int n,m,k=1;
    cin >> n;
    bool found[200] = {0};
    bool gj = true;
    while (n--) {
        cin >> m;
        k = max(k,m);
        found[m-1] = true;
    }

    for (int i = 0; i < k; i++) {
        if (!found[i]) {
            cout << i+1 << endl;
            gj = false;
        }
    }

    if (gj)
        cout << "good job";

    return 0;
}