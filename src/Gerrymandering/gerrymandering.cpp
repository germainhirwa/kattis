#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,n,v=0,wa=0,wb=0,d,va,vb;
    cin >> t >> n;
    vector<int> a(n,0), b(n,0);
    while (t--) {
        cin >> d >> va >> vb;
        v += va+vb;
        a[d-1] += va;
        b[d-1] += vb;
    }
    for (int i = 0; i < n; i++) {
        int mv = (a[i]+b[i])/2+1;
        if (a[i] > b[i]) {
            wb += b[i];
            wa += a[i]-mv;
            cout << "A " << a[i]-mv << " " << b[i] << endl;
        } else {
            wa += a[i];
            wb += b[i]-mv;
            cout << "B " << a[i] << " " << b[i]-mv << endl;
        }
    }
    printf("%.10lf",abs(wa-wb)/(double) v);
    return 0;
}