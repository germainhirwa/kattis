#include <iostream>
#include <string>
using namespace std;

int main()
{
    string word;
    cin >> word;

    int n = word.length();
    int ans = n;
    while (n--) {
        if (((word[n] == 'R') && (n % 3 == 2)) ||((word[n] == 'E') && (n % 3 == 1)) || ((word[n] == 'P') && (n % 3 == 0))) {
            ans--;
        }
    }

    cout << ans;
    return 0;
}