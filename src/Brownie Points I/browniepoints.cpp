#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    while (true) {
        vector<long> xpoints, ypoints;
        long x,y,s=0L,o=0L,xc,yc;

        cin >> n;
        if (n == 0) {
            break;
        }

        for (int i = 0; i < (n-1)/2; i++) {
            cin >> x >> y;
            xpoints.push_back(x);
            ypoints.push_back(y);
        }
        cin >> xc >> yc;
        for (int i = 0; i < (n-1)/2; i++) {
            if ((xpoints[i]-xc)*(ypoints[i]-yc) > 0) {
                s++;
            } else if ((xpoints[i]-xc)*(ypoints[i]-yc) < 0) {
                o++;
            }
            cin >> x >> y;
            if ((x-xc)*(y-yc) > 0) {
                s++;
            } else if ((x-xc)*(y-yc) < 0) {
                o++;
            }
        }

        cout << s << " " << o << endl;
    }
    return 0;
}