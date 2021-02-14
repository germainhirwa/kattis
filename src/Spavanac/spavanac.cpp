#include <iostream>
using namespace std;

int main()
{
    int h,m;
    cin >> h >> m;
    if (m < 45) {
        if (h < 1) {
            cout << 23 << " " << m+15;
        } else {
            cout << h-1 << " " << m+15;
        }
    } else {
        if (h < 1) {
            cout << 0 << " " << m-45;
        } else {
            cout << h << " " << m-45;
        }
    }
    return 0;
}