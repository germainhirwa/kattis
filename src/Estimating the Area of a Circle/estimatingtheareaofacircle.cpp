#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    double r, m, c;
    while (true) {
        cin >> r >> m >> c;
        if (r == 0 && m == 0 && c == 0) {
            break;
        }
        printf("%.10lf %.10lf\n",M_PI*pow(r,2), c/m*pow(2*r,2));
    }
    return 0;
}