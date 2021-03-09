#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    double w,g,h,r;
    cin >> n;
    while (n--) {
        cin >> w >> g >> h >> r;
        printf("%.10lf %.10lf\n",sqrt(w*w+(g-h)*(g-h)),sqrt(w*w+(g+h-2*r)*(g+h-2*r)));
    }

    return 0;
}