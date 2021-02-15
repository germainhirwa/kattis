#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int s,t,n;
    cin >> s >> t >> n;
    vector<int> bv, cv, dv;
    for (int i = 0; i < n+1; i++) {
        int d;
        cin >> d;
        dv.push_back(d);
    }
    for (int i = 0; i < n; i++) {
        int b;
        cin >> b;
        bv.push_back(b);
    }
    for (int i = 0; i < n; i++) {
        int c;
        cin >> c;
        cv.push_back(c);
    }
    int time = dv[0], stop = 1;
    while (stop <= n) {
        while (time % cv[stop-1] != 0) {
            time++;
        }
        time += bv[stop-1] + dv[stop];
        stop++;
    }
    cout << (time > t ? "no" : "yes");
    return 0;
}