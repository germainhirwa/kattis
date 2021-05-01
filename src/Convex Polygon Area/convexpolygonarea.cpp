#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,v,x,y,a;
    cin >> n;

    while (n--) {
        cin >> v;
        vector<int> xx, yy;
        a = 0;
        for (int i = 0; i < v; i++) {
            cin >> x >> y;
            xx.push_back(x);
            yy.push_back(y);
        }

        for (int i = 0; i < v; i++)
            a += xx[i]*yy[(i+1)%v] - xx[(i+1)%v]*yy[i];

        if (a % 2 == 0)
            cout << abs(a/2) << endl;
        else
            cout << abs(a/2.0) << endl;
    }

    return 0;
}