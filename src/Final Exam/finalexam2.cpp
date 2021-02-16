#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int count = 0;
    char prev = ' ';
    while (n--) {
        char x;
        cin >> x;
        if (prev == x) {
            count++;
        }
        prev = x;
    }
    cout << count;
    return 0;
}