import sys

def read_data(fname):
    data = []
    f = open(fname,"r")
    for line in f:
        line = line.strip()
        data.append(line)
    f.close()
    return data

def process(data):
    floor = 0  # starting position
    for line in data:
        for c in line:
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
    return floor

def day1(fname):
    data = read_data(fname)
    floor = process(data)
    print("floor = " + str(floor))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])

