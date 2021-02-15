#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n--) {
        string num;
        cin >> num;
        cout << num.length() << endl;
    }

    return 0;
}