#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main()
{
    int a,b,c,n1,n2,n3;
    string abc;

    cin >> n1 >> n2 >> n3 >> abc;
    c = max(n1,max(n2,n3));
    a = min(n1,min(n2,n3));

    if (n1 == a || n1 == c) {
        if (n2 == a || n2 == c) {
            b = n3;
        } else {
            b = n2;
        }
    } else {
        b = n1;
    }

    if (abc.compare("ABC") == 0) {
        cout << a << " " << b << " " << c;
    } else if (abc.compare("ACB") == 0) {
        cout << a << " " << c << " " << b;
    } else if (abc.compare("BAC") == 0) {
        cout << b << " " << a << " " << c;
    } else if (abc.compare("BCA") == 0) {
        cout << b << " " << c << " " << a;
    } else if (abc.compare("CAB") == 0) {
        cout << c << " " << a << " " << b;
    } else if (abc.compare("CBA") == 0) {
        cout << c << " " << b << " " << a;
    }
    return 0;
}