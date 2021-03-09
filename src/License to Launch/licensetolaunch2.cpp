#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int n, min = 1000000000, ans = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x < min) {
            min = x;
            ans = i;
        }
    }
    cout << ans;
    return 0;
}