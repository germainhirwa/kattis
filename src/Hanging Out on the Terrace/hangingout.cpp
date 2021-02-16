#include <iostream>
#include <string>
using namespace std;

int main()
{
    int l;
    int q;
    cin >> l >> q;

    int curr = 0;
    int count = 0;

    while (q--) {
        string c;
        int x;
        cin >> c >> x;
        if (c.compare("enter") == 0) {
            if (curr + x > l) {
                count++;
            } else {
                curr += x;
            }
        } else {
            curr -= x;
        }
    }
    cout << count;
    return 0;
}