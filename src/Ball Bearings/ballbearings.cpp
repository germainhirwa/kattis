#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t;
    double D,d,s;
    cin >> t;
    while (t--) {
        cin >> D >> d >> s;
        cout << (int) (M_PI/asin((s+d)/(D-d))) << endl;
    }

    return 0;
}