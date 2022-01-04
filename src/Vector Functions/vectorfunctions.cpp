#include "vectorfunctions.h"
#include <algorithm>

void backwards(std::vector<int>& vec){
    std::reverse(vec.begin(), vec.end());
}

std::vector<int> everyOther(const std::vector<int>& vec){
    std::vector<int> newVector;
    for (int i = 0; i < (int) vec.size(); i += 2) {
        newVector.push_back(vec[i]);
    }
    return newVector;
}

int smallest(const std::vector<int>& vec){
    int m = 2001;
    for (int i = 0; i < (int) vec.size(); i++) {
        m = min(m, vec[i]);
    }
    return m;
}

int sum(const std::vector<int>& vec){
    int s = 0;
    for (int i = 0; i < (int) vec.size(); i++) {
        s += vec[i];
    }
    return s;
}

int veryOdd(const std::vector<int>& suchVector){
    int n = 0;
    for (int i = 1; i < (int) suchVector.size(); i += 2) {
        if (suchVector[i] % 2 == 1) {
            n++;
        }
    }
    return n;
}