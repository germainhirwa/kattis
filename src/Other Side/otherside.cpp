#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    
    int w, s, c, k;
    cin >> w >> s >> c >> k;

    if (s < k || w + c < k || (s == k && w + c <= 2*k) || (w + c == k && s <= 2*k))
        cout << "YES";
    else
        cout << "NO";

    return 0;
}