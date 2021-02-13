#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int h;
    int v;
    cin >> h >> v;
    cout << ceil(h/sin(v*M_PI/180));
    return 0;
}