#include <iostream>
using namespace std;

int main()
{
    long n;
    cin >> n;
    int k = 0;
    int i = 2;
    while (i*i <= n) {
        if (n % i == 0) {
            n /= i;
            k++;
        } else {
            i ++;
        }
    }
    cout << k + (n == 1 ? 0 : 1);
    return 0;
}