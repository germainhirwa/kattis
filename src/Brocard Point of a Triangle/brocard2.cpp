#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int n, k;
    double x1, y1, x2, y2, x3, y3, a, b, c, d, e, f, AB2, BC2, AC2, A, B, C, w, x, y;
    cin >> n;

    while (n--) {
        cin >> k >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
        
        AB2 = pow(x2-x1,2)+pow(y2-y1,2);
        AC2 = pow(x3-x1,2)+pow(y3-y1,2);
        BC2 = pow(x3-x2,2)+pow(y3-y2,2);

        // Triangle angles
        A = acos((AB2+AC2-BC2)/(2*sqrt(AB2*AC2)));
        B = acos((AB2+BC2-AC2)/(2*sqrt(AB2*BC2)));
        C = acos((AC2+BC2-AB2)/(2*sqrt(AC2*BC2)));

        // Brocard angle
        w = atan(1.0/(cos(A)/sin(A) + cos(B)/sin(B) + cos(C)/sin(C)));

        // Using the rotation matrix by angle w
        a = (y2-y1)*cos(w) + (x2-x1)*sin(w);
        b = (y2-y1)*sin(w) - (x2-x1)*cos(w);
        c = (y1*(y2-y1) + x1*(x2-x1))*sin(w) + (x1*(y2-y1) - y1*(x2-x1))*cos(w);

        d = (y3-y2)*cos(w) + (x3-x2)*sin(w);
        e = (y3-y2)*sin(w) - (x3-x2)*cos(w);
        f = (y2*(y3-y2) + x2*(x3-x2))*sin(w) + (x2*(y3-y2) - y2*(x3-x2))*cos(w);

        // Intersection is the Brocard point
        x = (c*e-b*f)/(a*e-b*d);
        y = (c*d-a*f)/(b*d-a*e);

        // Final result
        cout << k << " " << x << " " << y << endl;
    }

    return 0;
}