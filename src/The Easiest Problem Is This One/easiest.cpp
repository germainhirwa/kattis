#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n = -1;
    while (n != 0) {
        cin >> n;
        if (n == 0) {
            return 0;
        }

        int p = 11;
        bool flag = true;
        int sd1 = 0, m = n;
        while (m) {
            sd1 += m % 10;
            m /= 10;
        }
        while (flag) {
            int sd2 = 0, t = n*p;
            while (t) {
                sd2 += t % 10;
                t /= 10;
            }
            if (sd1 == sd2) {
                flag = false;
                cout << p << endl;
            }

            p++;
        }

    }
    return 0;
}