import re, sys; input = sys.stdin.readline
quote = '''
UTC Coordinated Universal Time
GMT Greenwich Mean Time, defined as UTC
BST British Summer Time, defined as UTC+1 hour
IST Irish Summer Time, defined as UTC+1 hour
WET Western Europe Time, defined as UTC
WEST Western Europe Summer Time, defined as UTC+1 hour
CET Central Europe Time, defined as UTC+1
CEST Central Europe Summer Time, defined as UTC+2
EET Eastern Europe Time, defined as UTC+2
EEST Eastern Europe Summer Time, defined as UTC+3
MSK Moscow Time, defined as UTC+3
MSD Moscow Summer Time, defined as UTC+4
AST Atlantic Standard Time, defined as UTC-4 hours
ADT Atlantic Daylight Time, defined as UTC-3 hours
NST Newfoundland Standard Time, defined as UTC-3.5 hours
NDT Newfoundland Daylight Time, defined as UTC-2.5 hours
EST Eastern Standard Time, defined as UTC-5 hours
EDT Eastern Daylight Saving Time, defined as UTC-4 hours
CST Central Standard Time, defined as UTC-6 hours
CDT Central Daylight Saving Time, defined as UTC-5 hours
MST Mountain Standard Time, defined as UTC-7 hours
MDT Mountain Daylight Saving Time, defined as UTC-6 hours
PST Pacific Standard Time, defined as UTC-8 hours
PDT Pacific Daylight Saving Time, defined as UTC-7 hours
HST Hawaiian Standard Time, defined as UTC-10 hours
AKST Alaska Standard Time, defined as UTC-9 hours
AKDT Alaska Standard Daylight Saving Time, defined as UTC-8 hours
AEST Australian Eastern Standard Time, defined as UTC+10 hours
AEDT Australian Eastern Daylight Time, defined as UTC+11 hours
ACST Australian Central Standard Time, defined as UTC+9.5 hours
ACDT Australian Central Daylight Time, defined as UTC+10.5 hours
AWST Australian Western Standard Time, defined as UTC+8 hours
'''.strip().split('\n')
tz = {'UTC': 0}
for i in quote[1:]:
    gex = re.findall('UTC([\+\-\d\.]+)', i)
    if not gex: tz[i.split()[0]] = 0
    else: tz[i.split()[0]] = round(60*float(gex[0]))
for _ in range(int(input())):
    *t, s, d = input().strip().split()
    if t[0] == 'noon': t = ['12:00', 'p.m.']
    elif t[0] == 'midnight': t = ['12:00', 'a.m.']
    h, m = map(int, t[0].split(':')); h %= 12
    if t[1][0] == 'p': h += 12
    tt = (60*h+m+tz[d]-tz[s])%1440
    if tt == 0: print('midnight')
    elif tt == 720: print('noon')
    else:
        h, m = tt//60, str(tt%60).zfill(2)
        if h == 0: print(f'12:{m} a.m.')
        elif h == 12: print(f'12:{m} p.m.')
        elif h < 12: print(f'{h}:{m} a.m.')
        else: print(f'{h-12}:{m} p.m.')