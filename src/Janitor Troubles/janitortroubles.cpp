#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    double a,b,c,d;
    cin >> a >> b >> c >> d;
    double s = (a+b+c+d)/2;
    printf("%lf",sqrt((s-a)*(s-b)*(s-c)*(s-d)));
    return 0;
}