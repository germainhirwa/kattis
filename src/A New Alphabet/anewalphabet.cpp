#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    string s;
    getline(cin,s);
    map<int,string> dict;

    dict.insert(pair<int,string>(65,"@"));
    dict.insert(pair<int,string>(66,"8"));
    dict.insert(pair<int,string>(67,"("));
    dict.insert(pair<int,string>(68,"|)"));
    dict.insert(pair<int,string>(69,"3"));
    dict.insert(pair<int,string>(70,"#"));
    dict.insert(pair<int,string>(71,"6"));
    dict.insert(pair<int,string>(72,"[-]"));
    dict.insert(pair<int,string>(73,"|"));
    dict.insert(pair<int,string>(74,"_|"));
    dict.insert(pair<int,string>(75,"|<"));
    dict.insert(pair<int,string>(76,"1"));
    dict.insert(pair<int,string>(77,"[]\\/[]"));
    dict.insert(pair<int,string>(78,"[]\\[]"));
    dict.insert(pair<int,string>(79,"0"));
    dict.insert(pair<int,string>(80,"|D"));
    dict.insert(pair<int,string>(81,"(,)"));
    dict.insert(pair<int,string>(82,"|Z"));
    dict.insert(pair<int,string>(83,"$"));
    dict.insert(pair<int,string>(84,"']['"));
    dict.insert(pair<int,string>(85,"|_|"));
    dict.insert(pair<int,string>(86,"\\/"));
    dict.insert(pair<int,string>(87,"\\/\\/"));
    dict.insert(pair<int,string>(88,"}{"));
    dict.insert(pair<int,string>(89,"`/"));
    dict.insert(pair<int,string>(90,"2"));

    for (int i = 0; i < s.size(); i++) {
        if (65 <= s[i] && s[i] <= 90)
            cout << dict[(int) s[i]];
        else if (97 <= s[i] && s[i] <= 122)
            cout << dict[(int) s[i]-32];
        else
            cout << s[i];
    }

    return 0;
}