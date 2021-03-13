#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int a,b,c,n;
    cin >> a >> b >> c >> n;
    cout << ((a >= 1 && b >= 1 && c >= 1 && a+b+c >= n && n >= 3) ? "YES" : "NO");

    return 0;
}