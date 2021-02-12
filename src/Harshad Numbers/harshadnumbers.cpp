#include <iostream>
using namespace std;

int digitsum(int n);

int main()
{
    int n;
    cin >> n;

    while (n % digitsum(n) != 0) {
        n++;
    }

    cout << n;
    return 0;
}

int digitsum(int n) {
    int ans = 0;
    while (n != 0) {
        ans += n % 10;
        n /= 10;
    }
    return ans;
}