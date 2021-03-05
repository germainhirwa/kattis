i = 1
while True:
    line = input()
    if line == "END":
        break
    wp = 0
    for p in line:
        if p == ".":
            wp += 1
        elif wp != 0:
            break
    wp_list = line.split("*")[1:-1]
    if not wp_list:
        print(i, "EVEN")
    else:
        even = True
        for px in wp_list:
            if px != wp_list[0]:
                even = False
        if even:
            print(i, "EVEN")
        else:
            print(i, "NOT EVEN")
    i += 1