import sys
from math import *

r = 6371009
input()
for line in sys.stdin:
    lat1, long1, lat2, long2 = map(lambda x: float(x)*pi/180, line.split())
    d1 = r * acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(long2 - long1))
    d2 = r * hypot(hypot(cos(lat1)*cos(long1) - cos(lat2)*cos(long2), cos(lat1)*sin(long1) - cos(lat2)*sin(long2)), sin(lat1) - sin(lat2))
    print(abs(d1 - d2))