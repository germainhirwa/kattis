#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int a,b,c;
    cin >> a >> b >> c;
    cout << max(c-b,b-a)-1;
    return 0;
}