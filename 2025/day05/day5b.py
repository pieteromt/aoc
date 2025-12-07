import sys

def read_data(fname):
    ranges = []
    data = []
    dd = False
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        if len(line) == 0:
            dd = True
            continue
        if dd:
            data.append(int(line))
        else:
            ss = line.split('-')
            s0 = int(ss[0])
            s1 = int(ss[1])
            ranges.append((s0,s1))
    f.close()
    return ranges, data
    
def match(ranges, val):
    for r in ranges:
        if (val >= r[0]) and (val <= r[1]):
            return True
    return False

def myFunc(e):
    return e[0]

def process(ranges, data):
    ranges.sort(key=myFunc)
    cnt = 0
    B0 = 0
    E0 = 0
    for r in ranges:
        B1 = r[0]
        E1 = r[1]
        if B1 >= (E0+1):
            cnt += E1 - B1 + 1
        else:  # overlap
            if E1 > E0:
                cnt += (E1 - E0)
            else:
                pass
        B0 = B1
        E0 = E1
    print(cnt)

def day5(fname):
    ranges, data = read_data(fname)
    process(ranges, data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day5 input.txt") 
    else:
    	day5(sys.argv[1])
