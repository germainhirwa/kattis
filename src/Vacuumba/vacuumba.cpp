#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n, m;
    double x, y, d, ang, pos;
    cin >> n;
    
    while (n--) {
        cin >> m;
        x = 0;
        y = 0;
        pos = 90;
        while (m--) {
            cin >> ang >> d;
            pos += ang;
            x += d*cos(pos*M_PI/180);
            y += d*sin(pos*M_PI/180);
        }
        printf("%.7lf %.7lf\n",x,y);
    }

    return 0;
}