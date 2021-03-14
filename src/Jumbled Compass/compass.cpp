#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n1,n2;
    cin >> n1 >> n2;
    if (n1 >= n2) {
        n2 += 360;
    }
    if (n2-n1 > 180)
        cout << n2-n1-360;
    else
        cout << n2-n1;
    return 0;
}