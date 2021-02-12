#include <iostream>
using namespace std;

int main()
{
    int n, s;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;
        int maxX = 0;
        int minX = 99;
        for (int j = 0; j < s; j++) {
            int x;
            cin >> x;
            if (x > maxX) {
                maxX = x;
            }
            if (x < minX) {
                minX = x;
            }
        }
        
        cout << 2*(maxX-minX) << endl;
    }
    return 0;
}