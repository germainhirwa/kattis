#include <iostream>
using namespace std;

int main()
{
    long long ans = 2;
    int n;
    int exp = 1;
    
    cin >> n;
    
    while (exp < n) {
        ans *= 2;
        exp++;
    }

    ans++;
    cout << ans*ans;
    return 0;
}