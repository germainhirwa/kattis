#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int a,b,c,d,det,i=1;
    while (cin >> a >> b >> c >> d) {
        det = a*d-b*c;
        cout << "Case " << i << ":" << endl;
        cout << d/det << " " << -b/det << endl;
        cout << -c/det << " " << a/det << endl;
        i++;
    }

    return 0;
}