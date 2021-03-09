#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,k;
    cin >> n;
    while (n--) {
        cin >> k;
        cout << ceil(k/400.0) << endl;
    }

    return 0;
}