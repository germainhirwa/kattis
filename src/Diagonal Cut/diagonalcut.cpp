#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    long a,b,d;
    cin >> a >> b;
    d = __gcd(a,b);
    a /= d;
    b /= d;
    cout << (((a % 2) * (b % 2) == 1) ? d : 0);
    return 0;
}