#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,m,s;
    double tm=0,ts=0;
    cin >> n;
    while (n--) {
        cin >> m >> s;
        tm += m;
        ts += s;
    }

    if (ts/tm > 60)
        printf("%.10lf",ts/(60*tm));
    else
        cout << "measurement error";

    return 0;
}