#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    double r,h,s;
    while (true) {
        cin >> r >> h >> s;
        if (r == 0 && h == 0 && s == 0) {
            break;
        }
        printf("%.2f\n",(2*sqrt(h*h-r*r)+(2*M_PI-2*acos(r/h))*r)*(100+s)/100);
    }
    return 0;
}