#include <iostream>
#include <map>
using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        map<long, int> id;
        cout << "Case #" << i+1 << ": ";
        while (n--) {
            long x;
            cin >> x;
            if (id[x]) {
                id.erase(x);
            } else {
                id[x]++;
            }
        }
        cout << id.begin()->first << endl;
    }
    return 0;
}