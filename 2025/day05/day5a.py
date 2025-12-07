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

def process(ranges, data):
    sum = 0
    for d in data:
        if match(ranges, d):
            sum += 1
    print(sum)

def day5(fname):
    ranges, data = read_data(fname)
    process(ranges, data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day5 input.txt") 
    else:
    	day5(sys.argv[1])
