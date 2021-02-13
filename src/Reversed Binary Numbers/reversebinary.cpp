#include <iostream>
#include <stack>
#include <math.h>
using namespace std;

int main()
{
    int n;
    stack<int> s;
    cin >> n;
    int ex = floor(log2(n))+1; // resolve case power of 2
    while (ex--) {
        int el = n/pow(2,ex);
        s.push(el);
        n -= el*pow(2,ex);
    }

    int ans = 0;
    while (s.size()) {
        ans *= 2;
        ans += s.top();
        s.pop();
    }
    cout << ans;
    return 0;
}