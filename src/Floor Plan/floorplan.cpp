#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    cin >> n;
    
    if (n % 4 == 2)
        cout << "impossible";
    else if (n % 2 == 1)
        cout << (n + 1) / 2 << " " << (n - 1) / 2 ;
    else
        cout << (n / 4 + 1) << " " << (n / 4 - 1);

    return 0;
}