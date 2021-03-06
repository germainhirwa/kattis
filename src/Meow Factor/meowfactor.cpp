#include <iostream>
#include <math.h>

using namespace std;

int main() {
    long n, k;
    cin >> n;
    for (long m = 1; m < pow(n,1.0/9)+1; m++) {
        if (n % (m*m*m*m*m*m*m*m*m) == 0) {
            k = m;
        }
    }
    cout << k;
    return 0;
}