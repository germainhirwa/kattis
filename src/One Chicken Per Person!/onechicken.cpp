#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,m;
    cin >> n >> m;
    if (n < m)
        cout << "Dr. Chaz will have " << m-n << " piece" << ((m-n == 1) ? "" : "s") << " of chicken left over!";
    else
        cout << "Dr. Chaz needs " << n-m << " more piece" << ((n-m == 1) ? "" : "s") << " of chicken!";

    return 0;
}