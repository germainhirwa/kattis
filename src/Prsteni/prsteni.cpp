#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,p,r;
    cin >> n >> p;
    n--;
    while (n--) {
        cin >> r;
        cout << p/__gcd(p,r) << "/" << r/__gcd(p,r) << endl;
    }

    return 0;
}