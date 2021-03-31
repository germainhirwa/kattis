#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int x,y,x1,y1,x2,y2;
    cin >> x >> y >> x1 >> y1 >> x2 >> y2;

    int maxX = max(x1,x2), minX = min(x1,x2), maxY = max(y1,y2), minY = min(y1,y2);
    if (minY <= y && y <= maxY) {
        if (maxX <= x)
            cout << x-maxX;
        else if (x <= minX)
            cout << minX-x;
        else
            cout << 0;
    } else if (minX <= x && x <= maxX) {
        if (maxY <= y)
            cout << y-maxY;
        else if (y <= minY)
            cout << minY-y;
        else
            cout << 0;
    } else if (x <= minX) {
        if (y >= maxY)
            cout << hypot(y-maxY,minX-x);
        else // y <= minY
            cout << hypot(minY-y,minX-x);
    } else if (x >= maxX) {
        if (y >= maxY)
            cout << hypot(y-maxY,x-maxX);
        else // y <= minY
            cout << hypot(minY-y,x-maxX);
    } else
        cout << 0;

    return 0;
}