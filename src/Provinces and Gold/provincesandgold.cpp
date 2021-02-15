#include <iostream>
using namespace std;

int main()
{
    int g,s,c,bp;
    cin >> g >> s >> c;
    bp = 3*g + 2*s + c;
    bool flag = true;
    
    if (bp >= 8) {
        cout << "Province";
    } else if (bp >= 5) {
        cout << "Duchy";
    } else if (bp >= 2) {
        cout << "Estate";
    } else {
        flag = false;
    }

    if (flag) {
        cout << " or ";
    }

    if (bp >= 6) {
        cout << "Gold";
    } else if (bp >= 3) {
        cout << "Silver";
    } else {
        cout << "Copper";
    }
}