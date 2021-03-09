// Alternative way

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    long a,b;
    cin >> a >> b;
    cout << __gcd(2*a,2*b) - __gcd(2*a,b) - __gcd(a,2*b) + __gcd(a,b);
    return 0;
}