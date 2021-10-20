import sys

for line in sys.stdin:
    words = len(line.split())
    count = len(list(filter(lambda x: "ae" in x, words)))
    if count >= 0.4*words:
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")