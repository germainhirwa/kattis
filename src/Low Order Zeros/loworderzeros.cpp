#include <iostream>
#include <math.h>
using namespace std;

int solve(int n) {
    int trivial[] = {1,1,2,6,4,2,2,4,2,8}; // 0 to 9
    int power2[] = {6,2,4,8};
    // D(n) = 2^a * D(n/5) * D(n % 5)
    if (n < 10) {
        return trivial[n];
    } else {
        int k, a = n/5, b = n % 5;
        // k = 2^a mod 10
        k = power2[a % 4];
        return (k * solve(a) * solve(b)) % 10;
    }
}

int main()
{
    long n, f;
    while (true) {
        cin >> n;
        if (n == 0) {
            break;
        }
        cout << solve(n) << endl;
    }
    return 0;
}