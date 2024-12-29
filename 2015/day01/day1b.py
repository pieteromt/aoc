import sys

# input is a single line; nevertheless use an array of lines
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
    pos = 0
    for line in data:
        for c in line:
            pos += 1
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
            if floor == -1:  # basement reached?
                return pos
    return -1  # not found

def day1(fname):
    data = read_data(fname)
    pos = process(data)
    print("position = " + str(pos))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: day1 input.txt") 
    else:
    	day1(sys.argv[1])

