#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    vector<int> pos;
    int n,p,q,a,b,c;
    cin >> n >> q;
    while (n--) {
        cin >> p;
        pos.push_back(p);
    }
    while (q--) {
        cin >> c >> a >> b;
        switch (c) {
            case 1:
                pos[a-1] = b;
                break;
            case 2:
                cout << abs(pos[a-1]-pos[b-1]) << endl;
                break;
        }
    }

    return 0;
}