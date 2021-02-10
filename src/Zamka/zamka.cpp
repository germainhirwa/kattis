#include <iostream>
using namespace std;

int main()
{
    int l, d, x, temp, sd;
    int minsum = 10001;
    int maxsum = 0;
    cin >> l >> d >> x;
    for (int i = l; i <= d; i++) {
        temp = i;
        sd = 0;
        while (temp > 0) {
            sd += temp % 10;
            temp /= 10;
        }
        if (sd == x && i > maxsum) {
            maxsum = i;
        }
        if (sd == x && i < minsum) {
            minsum = i;
        }
    }

    cout << minsum << "\n" << maxsum;
    return 0;
}