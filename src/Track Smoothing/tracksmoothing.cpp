#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,r,p,x,y;
    double perimeter,scale;

    cin >> t;
    while (t--) {
        cin >> r >> p;
        perimeter = 0;
        vector<int> xx,yy;
        for (int i = 0; i < p; i++) {
            cin >> x >> y;
            xx.push_back(x);
            yy.push_back(y);
        }

        for (int i = 0; i < p; i++)
            perimeter += hypot(xx[i]-xx[(i+1)%p],yy[i]-yy[(i+1)%p]);
        scale = 1-2*M_PI*r/perimeter;

        if (0 < scale && scale < 1)
            cout << scale << endl;
        else
            cout << "Not possible" << endl;
    }
    return 0;
}