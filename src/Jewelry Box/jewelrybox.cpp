#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    double x,y,h;
    
    cin >> n;
    while (n--) {
        cin >> x >> y;
        h = (x + y - sqrt(x*x-x*y+y*y))/6;

        printf("%.10lf\n",(x-2*h)*(y-2*h)*h);
    }

    return 0;
}