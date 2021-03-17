#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t;
    int b[256];
    for (int i = 0; i < 256; i++) {
        int k = i^(2*i % 256);
        b[k] = i;
    }
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        cout << b[n] << " ";
    }

    return 0;
}