#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n--) {
        string s;
        cin >> s;
        int size = round(sqrt(s.length()));
        string arr[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                arr[size-1-j][i] = s[i*size+j];
            }
        }
        for (int m = 0; m < size; m++) {
            for (int n = 0; n < size; n++) {
                cout << arr[m][n];
            }
        }
        cout << endl;
    }
    return 0;
}