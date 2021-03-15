#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,p,k=0;
    double a1=0,a2=0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> p;
        a1 += p*pow(0.8,i);
        for (int j = 0; j < n-1; j++) {
            a2 += p*pow(0.8,k/n);
            k++;
        }
    }

    printf("%.10lf\n%.10lf",a1/5,a2/(5*n));

    return 0;
}