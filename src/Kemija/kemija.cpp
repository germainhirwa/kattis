#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    vector<string> words;
    string w;
    
    while (cin >> w) {
        words.push_back(w);
    }

    char vowels[] = {'a','e','i','o','u'};

    for (string word : words) {
        for (int i = 0; i < (int) word.length(); i++) {
            bool vowel = false;
            for (int j = 0; j < 5; j++) {
                if (word[i] == vowels[j]) {
                    vowel = true;
                    break;
                }
            }
            cout << word[i];
            if (vowel) {
                i += 2;
            }
        }
        cout << " ";
    }

    return 0;
}