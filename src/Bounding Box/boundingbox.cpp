#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n;
    double x1, y1, x2, y2, x3, y3, a, b, c, d, e, f, x, y, inc, maxX, minX, maxY, minY, currX, currY, tempX, tempY;

    while (true) {
        cin >> n;
        if (n == 0) {
            break;
        }

        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

        // Find the circumcenter by radius
        a = 2*(x2-x1);
        b = 2*(y2-y1);
        c = x2*x2 + y2*y2 - x1*x1 - y1*y1;

        d = 2*(x3-x2);
        e = 2*(y3-y2);
        f = x3*x3 + y3*y3 - x2*x2 - y2*y2;

        // X and Y are the coordinates of the circumcenter, R the radius
        x = (c*e-b*f)/(a*e-b*d);
        y = (c*d-a*f)/(b*d-a*e);

        // Initial angle
        inc = 2*M_PI/n;
        maxX = x1, maxY = y1, minX = x1, minY = y1, currX = x1, currY = y1;
        for (int i = 0; i < n; i++) { // use 0 again for double-check
            tempX = (currX-x)*cos(inc) - (currY-y)*sin(inc) + x;
            tempY = (currX-x)*sin(inc) + (currY-y)*cos(inc) + y;
            currX = tempX, currY = tempY;
            maxX = max(maxX,currX);
            maxY = max(maxY,currY);
            minX = min(minX,currX);
            minY = min(minY,currY);
        }

        // Final result
        printf("%.10lf\n", (maxX-minX)*(maxY-minY));
    }

    return 0;
}