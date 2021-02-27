#include <iostream>
#include <math.h>
#include <vector>
#include <utility>
using namespace std;

int main()
{
    int n,t;
    cin >> n >> t;
    vector<pair <double, double>> coords;
    double realdist = 0, gpsdist = 0;
    while (n--) {
        double xi,yi,ti,x,y;
        cin >> xi >> yi >> ti;
        if (coords.empty()) { // for t1
            pair <double,double> p1 (xi, yi);
            coords.push_back(p1);
        } else {
            pair <double, double> p2 (coords.back());
            realdist += sqrt(pow(xi-p2.first,2)+pow(yi-p2.second,2));
            int sz = (int) coords.size();
            for (int i = sz; i <= ti; i++) {
                x = (xi*(i-(sz-1)) + p2.first*(ti-i))/(ti-(sz-1));
                y = (yi*(i-(sz-1)) + p2.second*(ti-i))/(ti-(sz-1));
                pair <double, double> p (x,y);
                coords.push_back(p);
            }
        }
    }
    int k = (int) coords.size()-1;
    int i;
    for (i = t; i <= k; i += t) {
        gpsdist += sqrt(pow(coords[i].first-coords[i-t].first,2)+pow(coords[i].second-coords[i-t].second,2));
    }
    gpsdist += sqrt(pow(coords[k].first-coords[i-t].first,2)+pow(coords[k].second-coords[i-t].second,2));
    printf("%.15f",abs(realdist-gpsdist)/realdist*100);
    return 0;
}