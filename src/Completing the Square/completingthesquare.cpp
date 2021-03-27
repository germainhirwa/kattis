#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int x1,y1,x2,y2,x3,y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    int d12 = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
    int d13 = (x1-x3)*(x1-x3)+(y1-y3)*(y1-y3);
    int d23 = (x3-x2)*(x3-x2)+(y3-y2)*(y3-y2);
    if (d12 == d13)
        cout << x2+x3-x1 << " " << y2+y3-y1;
    else if (d12 == d23)
        cout << x1+x3-x2 << " " << y1+y3-y2;
    else // d13 == d23
        cout << x1+x2-x3 << " " << y1+y2-y3;

    return 0;
}