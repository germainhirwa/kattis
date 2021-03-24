#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    double e=0;
    cin >> n;
    for (int i = 0; i <= min(n,16); i++) {
        double f = 1;
        for (int j = 1; j <= i; j++) {
            f *= j;
        }
        e += 1/f;
    }
    printf("%.15lf",e);

    return 0;
}