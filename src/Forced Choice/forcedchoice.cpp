#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,p,s,t,c;
    cin >> n >> p >> s;
    while (s--) {
        cin >> t;
        bool rem = true;
        while (t--) {
            cin >> c;
            if (c == p)
                rem = false;
        }
        cout << (rem ? "REMOVE" : "KEEP") << endl;
    }

    return 0;
}