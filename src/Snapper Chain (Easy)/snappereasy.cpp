#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,n,k;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n >> k;
        cout << "Case #" << i << ": " << (((k+1) % (int) pow(2,n) == 0) ? "ON" : "OFF") << endl;
    }
    return 0;
}