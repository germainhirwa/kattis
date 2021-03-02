#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int D,V;
    while (true) {
        cin >> D >> V;
        if (D == 0 && V == 0) {
            break;
        }

        printf("%.10lf\n",pow(pow(D,3)-6*V/M_PI,1.0/3));
    }
    return 0;
}