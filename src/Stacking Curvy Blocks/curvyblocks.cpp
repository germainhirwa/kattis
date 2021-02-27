#include <iostream>
#include <math.h>
using namespace std;

double f(double x, double c0, double c1, double c2, double c3) {
    return c0 + c1*x + c2*pow(x,2) + c3*pow(x,3);
}

int main()
{
    double b0, b1, b2, b3, t0, t1, t2, t3, a0, a1, a2, a3, x1, x2, minf, maxf;
    while (cin >> b0 >> b1 >> b2 >> b3 >> t0 >> t1 >> t2 >> t3) {
        a0 = b0-t0;
        a1 = b1-t1;
        a2 = b2-t2;
        a3 = b3-t3;

        // Solve a1 + 2*a2*x + 3*a3*x^2 = 0
        x1 = (-a2 + sqrt(pow(a2,2)-3*a1*a3))/(3*a3);
        x2 = (-a2 - sqrt(pow(a2,2)-3*a1*a3))/(3*a3);
        minf = min(f(0,a0,a1,a2,a3),f(1,a0,a1,a2,a3));
        maxf = max(f(0,a0,a1,a2,a3),f(1,a0,a1,a2,a3));

        if (0 < x1 && x1 < 1) {
            minf = min(minf,f(x1,a0,a1,a2,a3));
            maxf = max(maxf,f(x1,a0,a1,a2,a3));
        }
        if (0 < x2 && x2 < 1) {
            minf = min(minf,f(x2,a0,a1,a2,a3));
            maxf = max(maxf,f(x2,a0,a1,a2,a3));
        }
        printf("%.6lf\n",maxf-minf);
    }
    return 0;
}