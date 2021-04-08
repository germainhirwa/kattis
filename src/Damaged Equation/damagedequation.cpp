#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int a,b,c,d;
    cin >> a >> b >> c >> d;

    bool e = false;

    if (a * b == c * d) {
        cout << a << " * " << b << " = " << c << " * " << d << endl;
        e  = true;
    }
    if (a * b == c + d) {
        cout << a << " * " << b << " = " << c << " + " << d << endl;
        e  = true;
    }
    if (a * b == c - d) {
        cout << a << " * " << b << " = " << c << " - " << d << endl;
        e  = true;
    }
    if (d != 0 && a * b == c / d) {
        cout << a << " * " << b << " = " << c << " / " << d << endl;
        e  = true;
    }
    if (a + b == c * d) {
        cout << a << " + " << b << " = " << c << " * " << d << endl;
        e  = true;
    }
    if (a + b == c + d) {
        cout << a << " + " << b << " = " << c << " + " << d << endl;
        e  = true;
    }
    if (a + b == c - d) {
        cout << a << " + " << b << " = " << c << " - " << d << endl;
        e  = true;
    }
    if (d != 0 && a + b == c / d) {
        cout << a << " + " << b << " = " << c << " / " << d << endl;
        e  = true;
    }
    if (a - b == c * d) {
        cout << a << " - " << b << " = " << c << " * " << d << endl;
        e  = true;
    }
    if (a - b == c + d) {
        cout << a << " - " << b << " = " << c << " + " << d << endl;
        e  = true;
    }
    if (a - b == c - d) {
        cout << a << " - " << b << " = " << c << " - " << d << endl;
        e  = true;
    }
    if (d != 0 && a - b == c / d) {
        cout << a << " - " << b << " = " << c << " / " << d << endl;
        e  = true;
    }
    if (b != 0 && a / b == c * d) {
        cout << a << " / " << b << " = " << c << " * " << d << endl;
        e  = true;
    }
    if (b != 0 && a / b == c + d) {
        cout << a << " / " << b << " = " << c << " + " << d << endl;
        e  = true;
    }
    if (b != 0 && a / b == c - d) {
        cout << a << " / " << b << " = " << c << " - " << d << endl;
        e  = true;
    }
    if (b != 0 && d != 0 && a / b == c / d) {
        cout << a << " / " << b << " = " << c << " / " << d << endl;
        e  = true;
    }

    if (!e)
        cout << "problems ahead";
    

    return 0;
}