#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,p,q;
    cin >> n >> p >> q;
    cout << (((p+q)/n) % 2 == 0 ? "paul" : "opponent");

    return 0;
}