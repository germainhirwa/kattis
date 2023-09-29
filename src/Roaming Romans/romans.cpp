#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    double x;
    cin >> x;
    cout << fixed << (int) round(x*880000/809);
    return 0;
}