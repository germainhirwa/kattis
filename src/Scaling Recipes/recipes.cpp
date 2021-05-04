#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t,r,p,d;
    string f;
    double w,c,s,b;

    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> r >> p >> d;
        s = (double) d/p;
        b = 0;
        vector<string> ss;
        vector<double> cc;

        printf("Recipe # %d\n",i);

        while (r--) {
            cin >> f >> w >> c;
            ss.push_back(f);
            cc.push_back(c);
            if (c == 100)
                b = w*s;
        }

        for (int j = 0; j < ss.size(); j++)
            printf("%s %.2lf\n",ss[j].c_str(),cc[j]*b/100);

        printf("----------------------------------------\n");
    }

    return 0;
}