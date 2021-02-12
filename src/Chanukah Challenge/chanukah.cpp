#include <iostream>
using namespace std;

int main()
{
    int n, no, c;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> no >> c;
        cout << no << " " << (c*(c+3))/2 << endl;
    }
    return 0;
}