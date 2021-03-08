#include <iostream>
#include <math.h>
using namespace std;

int main() {
    double n;
    cin >> n;
    printf("%.6lf",min(0.25,n*n/4));
    return 0;
}