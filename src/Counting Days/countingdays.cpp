#include "countingdays.h"

int day = 1;
int prev = 0;

void lookAtClock(int hours, int minutes) {
    if (hours*60+minutes < prev) day++;
    prev = hours*60+minutes;
}

int getDay() {
    return day;
}