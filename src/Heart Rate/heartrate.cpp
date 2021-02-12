#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int b;
        double p;
        cin >> b >> p;
        double ans = 60*b/p;
        double inc = 60/p;
        printf("%lf %lf %lf\n",ans-inc,ans,ans+inc);
    }
    return 0;
}