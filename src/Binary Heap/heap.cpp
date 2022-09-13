#include "heap.h"
#include <bits/stdc++.h>
using namespace std;

vector<int> v = {0};

int getMax() {
    return v[1];
}

int getSize() {
    return (int) v.size() - 1;
}

void shiftUp(int i) {
    while (i > 1 && v[i/2] < v[i]) {
        swap(v[i], v[i/2]);
        i /= 2;
    }
}

void shiftDown(int i) {
    int size = getSize();
    while (i <= size) {
        int maxV = v[i], maxId = i, left = 2*i, right = 2*i + 1;

        if (left <= size && maxV < v[left]) { 
            maxV = v[left];
            maxId = left;
        }

        if (right <= size && maxV < v[right]) {
            maxV = v[right];
            maxId = right;
        }

        if (maxId != i) {
            swap(v[maxId], v[i]);
            i = maxId;
        } else
            break;
    }
}

void insert(int element) {
    v.push_back(element);
    shiftUp(getSize());
}

void removeMax() {
    swap(v[1], v[getSize()]);
    v.pop_back();
    shiftDown(1);
}