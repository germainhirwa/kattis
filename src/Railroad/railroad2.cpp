#include <iostream>
using namespace std;

int main()
{
    int a,b;
    cin >> a >> b;
    cout << (b % 2 == 0 ? "possible" : "impossible");
    return 0;
}