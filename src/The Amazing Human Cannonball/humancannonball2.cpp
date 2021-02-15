#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n--) {
        double v, theta, x, h1, h2;
        cin >> v >> theta >> x >> h1 >> h2;
        double y = x*tan(theta*M_PI/180) - 4.905*pow(x,2)/(pow(v*cos(theta*M_PI/180),2));
        cout << ((h1 + 1 <= y && y <= h2 - 1) ? "Safe" : "Not Safe") << endl;
    }

    return 0;
}