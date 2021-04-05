#include <bits/stdc++.h>
using namespace std;

int sqd(int a, int b) {
    return a*a+b*b;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int q,x1,y1,x2,y2,x3,y3,a,b,c;

    cin >> q;
    for (int i = 0; i < q; i++) {
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
        a = sqd(x1-x2,y1-y2);
        b = sqd(x2-x3,y2-y3);
        c = sqd(x3-x1,y3-y1);

        cout << "Case #" << i+1 << ": ";

        if (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) == 0)
            cout << "not a triangle" << endl;
        else {
            if (a == b || b == c || c == a)
                cout << "isosceles ";
            else
                cout << "scalene ";
            
            if (a+b == c || b+c == a || c+a == b)
                cout << "right ";
            else if (a+b < c || b+c < a || c+a < b)
                cout << "obtuse ";
            else
                cout << "acute ";
            
            cout << "triangle" << endl;
        }
    }

    return 0;
}