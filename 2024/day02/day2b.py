import sys

def check(report, up):
    if up:
       d0 = 1
       d1 = 3
    else:
       d0 = -3
       d1 = -1
    nr = len(report)
    safe = True
    for i in range(0,nr-1):
        diff = report[i+1] - report[i]
        safe = (diff >= d0) and (diff <= d1)
        if not safe:
            break
    return safe

def check_damp(report, up):
    safe = check(report, up)
    if safe:
        #print("safe")
        return True
    # try with damping
    #print("not safe, damp")
    safe = True
    nr = len(report)
    for i in range(0,nr):
        rep = report.copy()
        rep.pop(i)   # remove one item
        safe = check(rep,up)
        if safe:
            break
    return safe

def is_safe(report):
    true = False
    up = True
    safe = True
    if report[0] == report[-1]:
        return False
    elif report[0] < report[-1]:
        up = True
        up_s = "True"
    else:
        up = False
        up_s = "False"
    #print("up = " + up_s)
    return check_damp(report, up)


def day2(fname):
    reports = []
    f = open(fname,"r")
    for line in f:
        numbers = line.strip().split()
        report = []
        i = 0
        for num in numbers:
            report.append(int(numbers[i]))
            i = i + 1
        reports.append(report)
    f.close()
    #print(reports)
    nr = 0
    for report in reports:
        if is_safe(report):
            nr = nr + 1
    print("nr = " + str(nr))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day2 input.txt") 
    else:
    	day2(sys.argv[1])

