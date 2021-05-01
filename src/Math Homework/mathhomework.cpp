#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int b,d,c,l;
    bool e = false;

    cin >> b >> d >> c >> l;
    for (int i = 0; i <= l/b; i++)
        for (int j = 0; j <= (l-b*i)/d; j++)
            for (int k = 0; k <= (l-b*i-d*j)/c; k++)
                if (b*i+d*j+c*k == l) {
                    e = true;
                    cout << i << " " << j << " " << k << endl;
                }

    if (!e)
        cout << "impossible";

    return 0;
}