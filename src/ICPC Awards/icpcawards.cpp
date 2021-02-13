#include <iostream>
#include <string>
using namespace std;

int main()
{
    string names[12][2];
    int n;
    int pos = 0;
    cin >> n;
    while (n--) {
        string univ, team;
        cin >> univ >> team;
        if (pos < 12) {
            bool flag = false;
            for (int j = 0; j < pos; j++) {
                if (univ.compare(names[j][0]) == 0) {
                    flag = true;
                }
            }
            if (!flag) {
                names[pos][0] = univ;
                names[pos][1] = team;
                pos++;
            }
        }
    }
    for (int i = 0; i < 12; i++) {
        cout << names[i][0] << " " << names[i][1] << endl;
    }

    return 0;
}