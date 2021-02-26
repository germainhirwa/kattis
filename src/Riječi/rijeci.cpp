#include <iostream>
using namespace std;

int main()
{
    int n,a = 0,b = 1,temp;
    cin >> n;
    for (int i = 0; i < n-1; i++) {
        temp = b;
        b = a+b;
        a = temp;
    }
    cout << a << " " << b;

    return 0;
}