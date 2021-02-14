#include <iostream>
#include <string>
#include <set> // for set implementations
using namespace std;

int main()
{
    int n;
    cin >> n;
    while (n--) {
        int t;
        cin >> t;
        set<string> places;
        while (t--) {
            string p;
            cin >> p;
            places.insert(p);
        }
        cout << places.size() << endl;
    }
    return 0;
}