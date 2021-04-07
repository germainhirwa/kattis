#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int D;
    cin >> D;
    if (D % 4 == 2)
        cout << "impossible";
    else if (D % 4 == 0)
        cout << (D/4-1) << " " << (D/4+1);
    else // D is odd
        cout << (D-1)/2 << " " << (D+1)/2;

    return 0;
}