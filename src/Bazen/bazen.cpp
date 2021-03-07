#include <iostream>
using namespace std;

int main() {
    double x,y,x1,y1;
    cin >> x >> y;
    if (x + y == 250) { // diagonal case
        if (x <= 125) { // the other endpoint lies on the x-axis
            x1 = 250-31250/(250-x);
            y1 = 0;
        } else { // x > 125, the other endpoint lies on the y-axis
            x1 = 0;
            y1 = 250-31250/x;
        }
    } else if (x == 0) { // lies on the y-axis
        if (y <= 125) { // the other endpoint lies on the diagonal
            x1 = 31250/(250-y);
            y1 = 250-x1;
        } else { // y > 125, the other endpoint lies on the x-axis
            x1 = 31250/y;
            y1 = 0;
        }
    } else { // lies on the x-axis
        if (x <= 125) { // the other endpoint lies on the diagonal
            x1 = 250-31250/(250-x);
            y1 = 250-x1;
        } else { // x > 125, the other endpoint lies on the y-axis
            x1 = 31250/x;
            y1 = 0;
        }
    }

    printf("%.2lf %.2lf",x1,y1);
    return 0;
}