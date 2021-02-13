#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<int> id;
        cout << "Case #" << i+1 << ": ";
        while (n--) {
            int x;
            cin >> x;
            if (count(id.begin(), id.end(), x)) {
                id.erase(find(id.begin(), id.end(), x));
            } else {
                id.push_back(x);
            }
        }
        cout << id[0] << endl;
    }
    return 0;
}