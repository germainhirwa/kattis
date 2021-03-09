import sys

for line in sys.stdin:
    a,b = line.split(" ")
    a,b = int(a),int(b)
    if 2**b >= a:
        print("Your wish is granted!")
    else:
        print("You will become a flying monkey!")