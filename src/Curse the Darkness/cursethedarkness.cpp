#include <iostream>
using namespace std;

int main()
{
    int n, k;
    double x,y,a,b;
    cin >> n;

    while (n--) {
        cin >> x >> y >> k;
        bool found = false;
        while (k--) {
            cin >> a >> b;
            if (!found) {
                if ((x-a)*(x-a)+(y-b)*(y-b) <= 64) {
                    found = true;
                }
            }
        }
        cout << (found ? "light a candle" : "curse the darkness") << endl;
    }
    return 0;
}