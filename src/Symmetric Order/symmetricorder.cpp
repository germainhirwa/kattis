#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n = -1;
    int count = 1;
    while (cin >> n) {
        if (n == 0) {
            break;
        }
        string arr[n];
        cout << "SET " << count << endl;
        for (int i = 0; i < n; i++) {
            string name;
            cin >> name;
            arr[i] = name;
        }
        for (int i = 0; i < n/2; i++) {
            cout << arr[2*i] << endl;
        }
        if (n % 2 == 1) {
            cout << arr[n-1] << endl;
        }
        for (int i = 0; i < n/2; i++) {
            cout << arr[n-1-2*i-(n%2)] << endl;
        }
        count++;
    }
    return 0;
}