#include <iostream>
#include <string>
#include <map>
using namespace std;

int main()
{
    int t, ans = 0, count = 0;
    map<string,int> logs;
    string p, status;
    
    while (true) {
        cin >> t;
        if (t == -1) {
            break;
        }
        cin >> p >> status;
        if (status.compare("right") == 0) {
            ans += t + 20*logs[p];
            count++;
        } else if (logs.count(p) == 0) {
            logs.insert(pair<string,int> (p,1));
        } else {
            logs.find(p)->second++;
        }
    }

    cout << count << " " << ans;

    return 0;
}