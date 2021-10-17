#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int n, w;
    cin >> w >> n;
    int ans = 0;
    while (n--) {
        int a,b;
        cin >> a >> b;
        ans += a*b;
    }
    cout << ans/w;
    return 0;
}