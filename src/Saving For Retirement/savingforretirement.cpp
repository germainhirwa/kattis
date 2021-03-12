#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    int a,b,c,d,e;
    cin >> a >> b >> c >> d >> e;
    cout << floor((b-a)*c/(double) e) + d + 1 << endl;

    return 0;
}