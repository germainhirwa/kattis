#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    cout << n << ":" << endl;
    for (int i = 2; i <= (n/2)+1; i++) {
        if ((n-i) % (2*i-1) == 0 || n % (2*i-1) == 0) {
            cout << i << "," << i-1 << endl;
        }
        if (n % i == 0) {
            cout << i << "," << i << endl;
        }
    }
    return 0;
}