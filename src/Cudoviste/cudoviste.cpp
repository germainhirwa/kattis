#include <iostream>
#include <string>
using namespace std;

int main() {
    int r,c;
    cin >> r >> c;
    char parking[r][c];
    
    for (int i = 0; i < r; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < c; j++) {
            parking[i][j] = row[j];
        }
    }

    int result[5] = {0,0,0,0,0};
    for (int i = 1; i < r; i++) {
        for (int j = 1; j < c; j++) {
            if (parking[i][j] != '#' && parking[i-1][j] != '#' && parking[i][j-1] != '#' && parking[i-1][j-1] != '#') {
                int count = 0;
                if (parking[i][j] == 'X') {
                    count++;
                }
                if (parking[i-1][j] == 'X') {
                    count++;
                }
                if (parking[i][j-1] == 'X') {
                    count++;
                }
                if (parking[i-1][j-1] == 'X') {
                    count++;
                }
                result[count]++;
            }
        }
    }

    for (int i = 0; i < 5; i++) {
        cout << result[i] << endl;
    }

    return 0;
}