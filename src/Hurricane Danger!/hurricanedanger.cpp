#include <iostream>
#include <math.h>
#include <vector>
#include <string>
using namespace std;

double sqdistance(int x, int y, int A, int B, int C) {
    return abs(((double) (A*x+B*y+C)*(A*x+B*y+C))/(A*A+B*B));
}

int main()
{
    int n,t;
    cin >> n ;
    while (n--) {
        int x1, y1, x2, y2, m, x, y, A, B, C;
        double mindist = 100000001;
        string city;
        cin >> x1 >> y1 >> x2 >> y2 >> m;
        vector<string> cities;
        A = y2-y1;
        B = x1-x2;
        C = (x2-x1)*y1 - (y2-y1)*x1;
        while (m--) {
            cin >> city >> x >> y;
            if (sqdistance(x,y,A,B,C) < mindist) {
                cities.clear();
                cities.push_back(city);
                mindist = sqdistance(x,y,A,B,C);
            } else if (sqdistance(x,y,A,B,C) == mindist) {
                cities.push_back(city);
            }
        }
        for (string c : cities) {
            cout << c << " ";
        }
        cout << endl;
    }
    return 0;
}