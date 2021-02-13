#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main()
{
    string n;
    cin >> n;

    if (n.compare("1") == 0) {
        cout << 1;
    } else if (n.compare("2") == 0) {
        cout << 2;
    } else if (n.compare("6") == 0) {
        cout << 3;
    } else if (n.compare("24") == 0) {
        cout << 4;
    } else if (n.compare("120") == 0) {
        cout << 5;
    } else if (n.compare("720") == 0) {
        cout << 6;
    } else {
        int digits = n.length();
        int num = 6;
        double init = 4*log10(2) + 2*log10(3) + log10(5);
        while (init < digits) {
            num++;
            init += log10(num);
        }
        cout << num-1;
    }

    return 0;
}