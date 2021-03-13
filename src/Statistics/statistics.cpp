#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,p,h,l,c=1;
    while (cin >> n) {
        h = -1000001, l = 1000001;
        while (n--) {
            cin >> p;
            h = max(h,p);
            l = min(l,p);
        }
        cout << "Case " << c << ": " << l << " " << h << " " << h-l << endl;
        c++;
    }

    return 0;
}