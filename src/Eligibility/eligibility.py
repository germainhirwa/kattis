import sys

for line in sys.stdin:
    if len(line.split()) != 1:
        name, pss, dob, courses = line.split()
        py, pm, pd = pss.split("/")
        by, bm, bd = dob.split("/")
        if int(py) >= 2010:
            print(name,"eligible")
        elif int(by) >= 1991:
            print(name,"eligible")
        elif int(courses) > 40:
            print(name,"ineligible")
        else:
            print(name,"coach petitions")