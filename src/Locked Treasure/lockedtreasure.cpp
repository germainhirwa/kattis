#include <iostream>
using namespace std;

long long choose (long long a, long long b) {
    if (a != 30) {
        long long ans = 1L;
        b = min(b,a-b);
        for (int i = 1; i <= b; i++) {
            ans *= (a+1-i);
        }
        for (int i = 1; i <= b; i++) {
            ans /= i;
        }
        return ans;
    } else { // a = 30, long long overflow
        if (b > 0) {
            return choose(29,b-1) + choose(29,b);
        } else {
            return 1;
        }
    }
}

int main()
{
    int n;
    long long ans;
    cin >> n;

    while (n--) {
        long long a, b; // return C(a,b-1)
        cin >> a >> b;
        cout << choose(a,b-1) << endl;
    }

    return 0;
}