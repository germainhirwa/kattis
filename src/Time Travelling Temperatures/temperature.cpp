#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int x,y;
    cin >> x >> y;
    if (y == 1) {
        if (x == 0)
            cout << "ALL GOOD";
        else
            cout << "IMPOSSIBLE";
    } else
        printf("%.10lf",((double) x)/(1-y));

    return 0;
}