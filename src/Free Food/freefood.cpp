#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    vector<bool> arr(365,false);
    int n, d1, d2, ans = 0;
    cin >> n;
    while (n--) {
        cin >> d1 >> d2;
        for (int i = d1; i <= d2; i++) {
            if (!arr[i-1])
                ans++;
            arr[i-1] = true;
        }
    }
    cout << ans;

    return 0;
}