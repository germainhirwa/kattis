#include <iostream>
#include <string>
using namespace std;

int main()
{
    string y,p;
    cin >> y >> p;
    if (y[y.length()-1] == 'e') {
        cout << y << "x" << p;
    } else if (y[y.length()-1] == 'a' || y[y.length()-1] == 'i' || y[y.length()-1] == 'o' || y[y.length()-1] == 'u') {
        cout << y.substr(0,y.length()-1) << "ex" << p;
    } else if (y.substr(y.length()-2,y.length()) == "ex") {
        cout << y << p;
    } else {
        cout << y << "ex" << p;
    }
    return 0;
}