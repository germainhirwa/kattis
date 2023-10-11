#include <bits/stdc++.h>
using namespace std;
const double PI = atan(1.0)*4;

vector<complex<double>> fft(vector<complex<double>> &coef, bool inverse) {
    int n = coef.size();
    if (n == 1) return coef;
    complex<double> z(0,0);
    vector<complex<double>> pe(n/2,z), po(n/2,z);
    for (int i = 0; i < n/2; i++) {
        pe[i] = coef[2*i];
        po[i] = coef[2*i+1];
    }
    vector<complex<double>> ye = fft(pe, inverse), yo = fft(po, inverse), y(n,z);
    double angle = (inverse ? -2 : 2)*PI/n;
    complex<double> w(cos(angle), sin(angle)), wj = 1;
    for (int j = 0; j < n/2; j++) {
        y[j] = ye[j] + wj*yo[j];
        y[j+n/2] = ye[j] - wj*yo[j];
        wj *= w;
    }
    return y;
}

vector<int> multiply(vector<complex<double>> &p1, vector<complex<double>> &p2) {
    int n = p1.size();
    vector<complex<double>> fft1 = fft(p1, false), fft2 = fft(p2, false), fftr;
    for (int i = 0; i < n; i++) fftr.push_back(fft1[i]*fft2[i]);
    vector<complex<double>> ifftr = fft(fftr, true);
    vector<int> result;
    for (int i = 0; i < n; i++) result.push_back(round(real(ifftr[i])/n));
    return result;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);
    string s;
    getline(cin, s);
    int nn=(int)s.size();
    vector<complex<double>> c1(nn), c2(nn);
    for (int i = 0; i < nn; i++) {
        if (s[i] == 'A') c1[nn-i-1] += 1.0;
        else c2[i] += 1.0;
    }
    int m = (int) pow(2, ceil(log2(2*nn-1)));
    for (int i = 0; i < m-nn; i++) c1.push_back(0);
    for (int i = 0; i < m-nn; i++) c2.push_back(0);
    vector<int> result = multiply(c1, c2);
    for (int i = nn-2; i >= 0; i--) cout << result[i] << '\n';
    return 0;
}