#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int size = 4;

    double arr[size];
    double inc = 1.0/s.length();
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '_') {
            arr[0] += inc;
        } else if (isupper(s[i])) {
            arr[2] += inc;
        } else if (islower(s[i])) {
            arr[1] += inc;
        } else {
            arr[3] += inc;
        }
    }

    while (size--) {
        cout << arr[3-size] << endl;
    }
    return 0;
}