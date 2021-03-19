#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    double r,c;
    cin >> r >> c;

    printf("%.10lf",100*pow((r-c)/r,2));

    return 0;
}