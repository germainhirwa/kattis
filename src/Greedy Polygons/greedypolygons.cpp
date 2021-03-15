#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,n,l,d,g;
    cin >> t;
    while (t--) {
        cin >> n >> l >> d >> g;
        cout << l*l*n/(tan(M_PI/n)*4) << " " << n*d*g*l << " " << M_PI*d*g*d*g << endl;
        printf("%.15lf\n",l*l*n*tan(M_PI/n)/4+n*d*g*l+M_PI*d*g*d*g);
    }

    return 0;
}