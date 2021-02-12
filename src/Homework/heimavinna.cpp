#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int ans = 0;
    cin >> s; // the whole line, will be dynamically modified
    string delimiter = ";";
    
    string::size_type sz;

    size_t pos = 0;
    string token;

    while ((pos = s.find(delimiter)) != string::npos) {
        token = s.substr(0, pos);
        size_t found = token.find("-");
        if (found != string::npos) { // there is a "-", say token = "aa-bbb"
            size_t pos2 = token.find("-");
            int a = stoi(token.substr(0,pos2),&sz);
            int b = stoi(token.substr(pos2+1,token.length()),&sz);
            ans += b-a+1;
        } else { // just a single question
            ans++;
        }
        s.erase(0, pos + delimiter.length());
    }

    // end of token
    size_t found = s.find("-");
    if (found != string::npos) { // there is a "-", say token = "aa-bbb"
        size_t pos2 = s.find("-");
        int a = stoi(s.substr(0,pos2),&sz);
        int b = stoi(s.substr(pos2+1,s.length()),&sz);
        ans += b-a+1;
    } else { // just a single question
        ans++;
    }
    
    cout << ans;
    return 0;
}