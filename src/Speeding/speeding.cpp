#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int q,t=0,s=0,tt,st,k=0;
    cin >> q;
    while (q--) {
        tt = t;
        st = s;
        cin >> t >> s;
        if (t > 0 && s > 0)
            k = max(k,(s-st)/(t-tt));
    }
    cout << k;

    return 0;
}