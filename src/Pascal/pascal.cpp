#include <iostream>
#include <vector>
using namespace std;

int main()
{
    long n;
    cin >> n;
    if (n == 1) {
        cout << 0;
    } else {
        long i = 2;
        while (i*i <= n) {
            if (n % i == 0) {
                cout << n-n/i;
                return 0;
            }
            i++;
        }
        cout << n-1;
    }
    return 0;
}