#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    string word;
    vector<string> words;
    while (cin >> word) {
        for (int i = 0; i < words.size(); i++) {
            if (words[i] == word) {
                cout << "no";
                return 0;
            }
        }
        words.push_back(word);
    }
    cout << "yes";
    return 0;
}