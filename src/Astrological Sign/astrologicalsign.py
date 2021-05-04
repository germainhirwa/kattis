import sys

def horoscope(d,m):
    if m == 'Jan':
        if 1 <= d <= 20:
            return 'Capricorn'
        else:
            return 'Aquarius'
    elif m == 'Feb':
        if 1 <= d <= 19:
            return 'Aquarius'
        else:
            return 'Pisces'
    elif m == 'Mar':
        if 1 <= d <= 20:
            return 'Pisces'
        else:
            return 'Aries'
    elif m == 'Apr':
        if 1 <= d <= 20:
            return 'Aries'
        else:
            return 'Taurus'
    elif m == 'May':
        if 1 <= d <= 20:
            return 'Taurus'
        else:
            return 'Gemini'
    elif m == 'Jun':
        if 1 <= d <= 21:
            return 'Gemini'
        else:
            return 'Cancer'
    elif m == 'Jul':
        if 1 <= d <= 22:
            return 'Cancer'
        else:
            return 'Leo'
    elif m == 'Aug':
        if 1 <= d <= 22:
            return 'Leo'
        else:
            return 'Virgo'
    elif m == 'Sep':
        if 1 <= d <= 21:
            return 'Virgo'
        else:
            return 'Libra'
    elif m == 'Oct':
        if 1 <= d <= 22:
            return 'Libra'
        else:
            return 'Scorpio'
    elif m == 'Nov':
        if 1 <= d <= 22:
            return 'Scorpio'
        else:
            return 'Sagittarius'
    elif m == 'Dec':
        if 1 <= d <= 21:
            return 'Sagittarius'
        else:
            return 'Capricorn'

for line in sys.stdin:
    dm = line.strip().split(" ")
    if len(dm) == 2:
        print(horoscope(int(dm[0]),dm[1]))