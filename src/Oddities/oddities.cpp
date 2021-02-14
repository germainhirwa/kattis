#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n--) {
        int x;
        cin >> x;
        cout << x << " is " << ((x % 2 == 0) ? "even" : "odd") << endl;
    }
    return 0;
}