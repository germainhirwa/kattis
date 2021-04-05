#include <bits/stdc++.h>
using namespace std;

double area(int x1, int y1, int x2, int y2, int x3, int y3) {
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int x1,y1,x2,y2,x3,y3,t,x,y,c=0;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    double d = area(x1,y1,x2,y2,x3,y3);
    printf("%.1lf\n",d);

    cin >> t;
    while (t--) {
        cin >> x >> y;
        if (area(x1,y1,x2,y2,x,y) + area(x1,y1,x3,y3,x,y) + area(x3,y3,x2,y2,x,y) == d)
            c++;
    }
    printf("%d",c);

    return 0;
}